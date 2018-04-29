import json
import pymysql
import getpass
import sys
import datetime

"""
    這個程式會把CVEjson檔案輸出至local database。
    使用方法: python cve_json_to_sql.py [json_directory] [database_name]
"""
#Store all the table names.
table_names = ["CVE_header","CVE_content","CVE_vendor","CVE_product","CVE_to_product"]
def cve_json_to_sql(json_directory,database_name):

    #Get the username and password of database
    username = input("Please enter local database Username:")
    password = getpass.getpass("Local database Password:")

    #Try to connect to the database
    try:
        print("Connect to database "+database_name+"...")
        db = pymysql.connect("localhost",username,password,database_name,use_unicode=True, charset="utf8")
    except:
        print("Error while connecting database.")
        return
    
    #Create mysql cursor
    cursor = db.cursor()

#--------------------------------------------Create tables -------------------------------------------------

    #The flag will be True if all table are exist
    is_all_exist = True
    #Check if the tables are all exist.
    for table in table_names:
        if not is_table_exist(cursor,table):
            is_all_exist = False    #Set flag to false
    if is_all_exist:
        c = input("Tables are already exist.Do you want to drop them and create new ones(Y/n)?")
        if c=='Y' or c=='y':
            #Drop the former table.
            sql = """DROP TABLE IF exists """+table_names[4]+"""
                    DROP TABLE IF exists """+table_names[3]+"""
                    DROP TABLE IF exists """+table_names[2]+"""
                    DROP TABLE IF exists """+table_names[1]+"""
                    DROP TABLE IF exists """+table_names[0]
            for s in sql.split('\n'):
                if len(s)<=1:
                    continue
                cursor.execute(s)
            is_all_exist=False
            db.commit()
            print("Already drops all tables.")
        elif c=='N' or c=='n':
            print("Appending data to the table.")
        else:
            print("Input error.Appending data to the table.")
    if not is_all_exist:
        #Create tables        
        for table in table_names:
            if not is_table_exist(cursor,table):
            # The table is missing or has not been created yet.
            # Create a new table for it.
                create_CVE_table(cursor,table)

#--------------------------------------------Get data from json-------------------------------------------------
    
    import os

    for filename in os.listdir(json_directory):
        #Use to store json data
        jsondata = []
        if(filename[-5:]==".json"):
            print("Parsing "+filename+":")

            #Load the json data
            with open(json_directory+"/"+filename,encoding='utf-8') as jsonf:
                print("\tLoading json data...")
                tmp = json.loads(jsonf.read())
                for line in tmp:
                    jsondata.append(line)
            
            #get the first element(Actually equals all data)
            jsondata = jsondata[0]

            '''
            #Get the navigation
            try:
                jsondata = jsondata[0]
                navigation = jsondata['navigation']
            except:
                #if There is no navigation
                print("Navigation is not found.Continue next step.")
            '''
            
            #json data to sql format
            print("\tInsert data to table...")

            #Get the last id of tables
            vendorid_count = get_last_id_of_table(cursor,table_names[2])+1
            productid_count = get_last_id_of_table(cursor,table_names[3])+1

            for item in jsondata['CVE_Items']:
                #避免重複
                if is_CVE_id_exist(cursor,item['cve']['CVE_data_meta']['ID'])==False:

                    #Get the CVE id
                    CVE_id=item['cve']['CVE_data_meta']['ID']

                    #Get CVSS score
                    try:
                        item['impact']['baseMetricV2']['cvssV2']['baseScore']
                        score = item['impact']['baseMetricV2']['cvssV2']['baseScore']
                    except:
                        score=None
                    #print(CVE_id)
                    #Insert CVE_header
                    sql = """insert into """+table_names[0]+"""(CVE_id,PublishedDate,LastModifiedDate,Score)
                            values (%s,%s,%s,%s);
                        """
                    cursor.execute(sql,(CVE_id,
                                        date_to_datetime(item['publishedDate']),
                                        date_to_datetime(item['lastModifiedDate']),
                                        score
                                        ))
                    
                    #Insert CVE_content
                    sql = """insert into """+table_names[1]+"""(CVE_id,CVE_description)
                            values (%s,%s);
                        """
                    cursor.execute(sql,(CVE_id,
                                        item['cve']['description']['description_data'][0]['value']
                                        ))

                    #Parsing the vendor id
                    vendors=item['cve']['affects']['vendor']['vendor_data']
                    for v in vendors:
                        vendor_name = v['vendor_name']
                        tmpid = get_vendor_id(cursor,vendor_name)
                        if tmpid!=0:
                            #The vendor has been store in table.
                            vendorid = tmpid
                        else:
                            #Vendor not be found in table.Create a new vendor information.
                            vendorid = vendorid_count
                            vendorid_count = vendorid_count + 1

                            #Insert CVE_vendor
                            sql = """insert into """+table_names[2]+"""(Vendor_id,Vendor_name)
                                    values (%s,%s);
                                """
                            cursor.execute(sql,(vendorid,
                                                vendor_name)
                                        )        
                    #Insert CVE_product and CVE_to_product
                    for v in vendors:
                        #Get the product list
                        products = v['product']['product_data']
                        vendor_name = v['vendor_name']
                        for t in products:
                            #Get the product name
                            product_name = t['product_name']

                            #Store different product versions
                            for ver in t['version']['version_data']:
                                #Parsing the product id
                                if ver['version_value']=='*':
                                    ver['version_value']='all'
                                tmpid = get_product_id(cursor,product_name,ver['version_value'])
                                if tmpid!=0:
                                    #The version of product has been stored in table.
                                    productid = tmpid
                                else:
                                    #This version of product is not found in table.
                                    #Create a new product information.
                                    productid = productid_count
                                    productid_count = productid_count + 1

                                    #Insert into CVE_product table
                                    sql = """insert into """+table_names[3]+"""(product_id,product_name,vendor_id,product_ver)
                                        values (%s,%s,%s,%s);
                                    """
                                    cursor.execute(sql,(productid,
                                                        product_name,
                                                        get_vendor_id(cursor,vendor_name),
                                                        ver['version_value']
                                                    ))
                                #Insert CVE_to_product
                                sql = """insert into """+table_names[4]+"""(CVE_id,product_id)
                                        values (%s,%s);
                                    """
                                cursor.execute(sql,(CVE_id,
                                                    productid
                                                    ))

                    db.commit()

    db.close()
    print("Finish")

def is_table_exist(cursor,table_name):
    #Check if table_name table exists.
    sql = "SHOW TABLES LIKE '"+table_name+"';"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False
def get_last_id_of_table(cursor,table_name):
    #Get the last id of table by counting the table
    sql = "select count(*) from "+table_name+";"
    cursor.execute(sql)
    result = cursor.fetchone()

    return result[0]
def is_CVE_id_exist(cursor,CVE_id):
    #Check if the CVE_id is exist.
    sql = "select CVE_id from "+table_names[0]+" where CVE_id=%s;"
    cursor.execute(sql,CVE_id)
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False
def get_vendor_id(cursor,vendor_name):
    #Use the vendor_name to get the vendor id.
    #It will return 0 if is doesn't exist.
    sql = "select Vendor_id from "+table_names[2]+" where vendor_name=%s;"
    cursor.execute(sql,vendor_name)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0
    return 0
def get_product_id(cursor,product_name,product_ver):
    #Use the product_name and product_ver to get the product id.
    #It will return 0 if is doesn't exist.
    sql = "select product_id,product_ver from "+table_names[3]+" where product_name=%s;"
    cursor.execute(sql,(product_name))
    result = cursor.fetchall()
    if result:
        for r in result:
            if r[1]==product_ver:
                return r[0]
        return 0
    else:
        return 0
    return 0
def date_to_datetime(date):
    import time
    
    if date=="":
        return None
    else:
        t = time.strptime(date, "%Y-%m-%dT%H:%MZ")
        return t
def create_CVE_table(cursor,table_name):
    if table_name==table_names[0]:
        #create CVE_header table
        create_CVE_header_table(cursor)

    elif table_name==table_names[1]:
        #create CVE_content table
        create_CVE_content_table(cursor)

    elif table_name==table_names[2]:
        #create CVE_vendor table
        create_CVE_vendor_table(cursor)

    elif table_name==table_names[3]:
        #create CVE_product table
        create_CVE_product_table(cursor)

    elif table_name==table_names[4]:
        #create CVE_to_product table
        create_CVE_to_product_table(cursor)
    else:
        print("Table name error.")

def create_CVE_header_table(cursor):
    #create the data format of table
    #all encode with utf-8
    table_name = "CVE_header"
    print("Creating table "+table_name+" ...")
    sql = """
            create table """+table_name+""" (
                CVE_id varchar(30) primary key,
                PublishedDate datetime,
                LastModifiedDate datetime,
                Score numeric(3,1)
            ); """
    cursor.execute(sql)
def create_CVE_content_table(cursor):
    #create the data format of table
    #all encode with utf-8
    table_name = "CVE_content"
    print("Creating table "+table_name+" ...")
    sql = """
            create table """+table_name+""" (
                CVE_id varchar(30) primary key,
                CVE_description text character set utf8mb4,
                Foreign key(CVE_id) references CVE_header(CVE_id)

            ); """
    cursor.execute(sql)
def create_CVE_vendor_table(cursor):
    #create the data format of table
    #all encode with utf-8
    table_name = "CVE_vendor"
    print("Creating table "+table_name+" ...")
    sql = """
            create table """+table_name+""" (
                Vendor_id int primary key,
                Vendor_name varchar(100) character set utf8

            ); """
    cursor.execute(sql)
def create_CVE_product_table(cursor):
    #create the data format of table
    #all encode with utf-8
    table_name = "CVE_product"
    print("Creating table "+table_name+" ...")
    sql = """
            create table """+table_name+""" (
                Product_id int primary key,
                Product_name varchar(100) character set utf8,
                Vendor_id int,
                Product_ver varchar(100) character set utf8,
                Foreign key(vendor_id) references CVE_vendor(vendor_id)

            ); """
    cursor.execute(sql)
def create_CVE_to_product_table(cursor):
    #create the data format of table
    #all encode with utf-8
    table_name = "CVE_to_product"
    print("Creating table "+table_name+" ...")
    sql = """
            create table """+table_name+""" (
                CVE_id varchar(30) character set utf8,
                Product_id int

            ); """
    cursor.execute(sql)

def remove_non_ascii(text):
    return normalize('NFKD', text).encode('ascii','ignore')
#--------------------------------------main function-----------------------------------------
json_directory = sys.argv[1]
database_name = sys.argv[2]
cve_json_to_sql(json_directory,database_name)