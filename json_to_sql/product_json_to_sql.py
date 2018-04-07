import json
import pymysql
import getpass
import sys
"""
    這個程式會把太陽能產品資料json檔案輸出至local database。
    使用方法: python product_json_to_sql.py [json_name] [database_name]
"""
def product_json_to_sql(json_name,database_name):

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

    #Create table "solar_product"
    #This operation will override the table if it exists.
    sql = "DROP TABLE IF exists solar_product"
    cursor.execute(sql)

    #create the data format of table
    #all encode with utf-8
    print("Creating table solar_product...")
    sql = """
            create table solar_product(
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
    db.commit() 

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
    db.commit()
    db.close()
    print("Finish")
json_name = sys.argv[1]
database_name = sys.argv[2]
product_json_to_sql(json_name,database_name)