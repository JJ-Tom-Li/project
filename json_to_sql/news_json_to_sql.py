import json
import pymysql
import getpass
import sys
"""
    這個程式會把資安新聞json檔案輸出至local database。
    文章部分會用txt檔另存
    使用方法: 
        python news_json_to_sql.py [json_directory] [database_name] [news_source]
"""
def news_json_to_sql(json_directory,database_name,news_source):

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
    #Store all the table names.
    table_names = ["News_header","News_content","News_topic","News_to_topic","News_author"]
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
            sql = """DROP TABLE IF exists News_header
                    DROP TABLE IF exists News_content
                    DROP TABLE IF exists News_topic
                    DROP TABLE IF exists News_to_topic
                    DROP TABLE IF exists News_author"""
            for s in sql.split('\n'):
                if len(s)<=1:
                    continue
                print(s)
                cursor.execute(s)
            #db.commit()
            print("Already drops all tables.")
        elif c=='N' or c=='n':
            print("Appending data to the table.")
        else:
            print("Input error.Appending data to the table.")
    #Create tables        
    for table in table_names:
        if not is_table_exist(cursor,table):
           # The table is missing or has not been created yet.
            # Create a new table for it.
            create_News_table(cursor,table)
#--------------------------------------------Get data from json-------------------------------------------------
    '''
    #TODO
    #Use to store json data
    jsondata = []

    #Load the json data
    with open(json_name,encoding='utf-8') as jsonf:
        print("Loading json data...")
        tmp = json.loads(jsonf.read())
        for line in tmp:
            jsondata.append(line)
    
    #json data to sql format
    print("Insert data to table...")
    for item in jsondata:
        sql = """insert into solar_product(登錄編號,廠牌,型號,額定功率,輸入電壓,輸出電壓,登錄有效期限,相關認證,備註)
                 values (%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        cursor.execute(sql,(
            item['登錄編號'],item['廠牌'],item['型號'],item['額定功率(W)'],item['輸入電壓(V)']
            ,item['輸出電壓(V)'],item['登錄有效期限'],item['相關認證(註1)'],item['備註']))
    db.commit()'''
    db.close()
    print("Finish")

def is_table_exist(dbcursor,table_name):
    #Check if table_name table exists.
    sql = "SHOW TABLES LIKE '"+table_name+"';"
    dbcursor.execute(sql)
    result = dbcursor.fetchone()
    if result:
        return True
    else:
        return False
def create_News_table(cursor,table_name):
    if table_name=="News_header":
        create_News_header_table(cursor)
    elif table_name=="News_content":
        create_News_content_table(cursor)
    elif table_name=="News_topic":
        create_News_topic_table(cursor)
    elif table_name=="News_to_topic":
        create_News_to_topic_table(cursor)
    elif table_name=="News_author":
        create_News_author_table(cursor)
    else:
        print("Table name error.")

def create_News_header_table(cursor):
    #create the data format of table
    #all encode with utf-8
    table_name = "News_header"
    print("Creating table "+table_name+" ...")
    #TODO:
    sql = """
            create table """+table_name+""" (
                登錄編號 varchar(30) NOT NULL,
                廠牌 varchar(100) character set utf8,
                型號 varchar(100) character set utf8,
                額定功率 varchar(20) character set utf8,
                輸入電壓 varchar(30) character set utf8,
                輸出電壓 varchar(30) character set utf8,
                登錄有效期限 varchar(100) character set utf8,
                相關認證 varchar(100) character set utf8,
                備註 varchar(100) character set utf8
            ); """
    cursor.execute(sql)
def create_News_content_table(cursor):
    #TODO:
    #create the data format of table
    #all encode with utf-8
    table_name = "News_content"
    print("Creating table "+table_name+" ...")
    sql = """
            create table """+table_name+""" (
                登錄編號 varchar(30) NOT NULL,
                廠牌 varchar(100) character set utf8,
                型號 varchar(100) character set utf8,
                額定功率 varchar(20) character set utf8,
                輸入電壓 varchar(30) character set utf8,
                輸出電壓 varchar(30) character set utf8,
                登錄有效期限 varchar(100) character set utf8,
                相關認證 varchar(100) character set utf8,
                備註 varchar(100) character set utf8
            ); """
    cursor.execute(sql)
def create_News_topic_table(cursor):
    #TODO:
    #create the data format of table
    #all encode with utf-8
    table_name = "News_topic"
    print("Creating table "+table_name+" ...")
    sql = """
            create table """+table_name+""" (
                登錄編號 varchar(30) NOT NULL,
                廠牌 varchar(100) character set utf8,
                型號 varchar(100) character set utf8,
                額定功率 varchar(20) character set utf8,
                輸入電壓 varchar(30) character set utf8,
                輸出電壓 varchar(30) character set utf8,
                登錄有效期限 varchar(100) character set utf8,
                相關認證 varchar(100) character set utf8,
                備註 varchar(100) character set utf8
            ); """
    cursor.execute(sql)
def create_News_to_topic_table(cursor):
    #TODO:
    #create the data format of table
    #all encode with utf-8
    table_name = "News_to_topic"
    print("Creating table "+table_name+" ...")
    sql = """
            create table """+table_name+""" (
                登錄編號 varchar(30) NOT NULL,
                廠牌 varchar(100) character set utf8,
                型號 varchar(100) character set utf8,
                額定功率 varchar(20) character set utf8,
                輸入電壓 varchar(30) character set utf8,
                輸出電壓 varchar(30) character set utf8,
                登錄有效期限 varchar(100) character set utf8,
                相關認證 varchar(100) character set utf8,
                備註 varchar(100) character set utf8
            ); """
    cursor.execute(sql)
def create_News_author_table(cursor):    
    #TODO:
    #create the data format of table
    #all encode with utf-8
    table_name = "News_author"
    print("Creating table "+table_name+" ...")
    sql = """
            create table """+table_name+""" (
                登錄編號 varchar(30) NOT NULL,
                廠牌 varchar(100) character set utf8,
                型號 varchar(100) character set utf8,
                額定功率 varchar(20) character set utf8,
                輸入電壓 varchar(30) character set utf8,
                輸出電壓 varchar(30) character set utf8,
                登錄有效期限 varchar(100) character set utf8,
                相關認證 varchar(100) character set utf8,
                備註 varchar(100) character set utf8
            ); """
    cursor.execute(sql)
json_directory = sys.argv[1]
database_name = sys.argv[2]
news_source = sys.argv[3]
news_json_to_sql(json_directory,database_name,news_source)