import json
import pymysql
import getpass
import sys
import datetime
"""
    這個程式會把資安新聞json檔案輸出至local database。
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
                create_News_table(cursor,table)
#--------------------------------------------Get data from json-------------------------------------------------
    
    #TODO
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

            #Get the navigation
            jsondata = jsondata[0]
            navigation = jsondata['navigation']
            
            #json data to sql format
            print("\tInsert data to table...")

            #Get the last id of tables
            newsid = get_last_id_of_table(cursor,"News_header")+1
            authorid = get_last_id_of_table(cursor,"News_author")+1
            topicid = get_last_id_of_table(cursor,"News_topic")+1

            for item in jsondata['news_list']:
                #避免重複
                if get_news_id(cursor,item['title']) ==0:
                    #Insert News_header
                    sql = """insert into News_header(News_id,Title,Date,author_id,News_source)
                            values (%s,%s,%s,%s,%s);
                        """
                    cursor.execute(sql,(newsid,
                                        item['title'],
                                        date_to_datetime(item['date']),
                                        get_author_id(cursor,item['author']),
                                        news_source
                                        ))
                    #Insert News_content
                    #Insert News_topic
                    #Insert News_to_topic
                    #Insert News_author
                    newsid = newsid+1
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
def get_news_id(cursor,news_name):
    #Use the news title to get the news id.
    #It will return 0 if is doesn't exist.
    sql = "select News_id from News_header where title=%s;"
    cursor.execute(sql,news_name)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0
def get_author_id(cursor,author_name):
    #Use the author_name to get the author id.
    #It will return 0 if is doesn't exist.
    sql = "select Author_id from News_author where author_name=%s;"
    cursor.execute(sql,author_name)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0
    return 0
def get_topic_id(cursor,topic):
    #Use the topic_name to get the topic id.
    #It will return 0 if is doesn't exist.
    sql = "select topic_id from News_author where topic_name=%s;"
    cursor.execute(sql,topic)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0
    return 0
def date_to_datetime(date):
    return None
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
    sql = """
            create table """+table_name+""" (
                News_id int PRIMARY KEY,
                Title varchar(200) character set utf8,
                Date datetime,
                author_id int,
                News_source varchar(50) character set utf8
            ); """
    cursor.execute(sql)
def create_News_content_table(cursor):
    #create the data format of table
    #all encode with utf-8
    table_name = "News_content"
    print("Creating table "+table_name+" ...")
    sql = """
            create table """+table_name+""" (
                News_id int primary key,
                News_link varchar(200) character set utf8,
                News_body text
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
                News_topic int primary key,
                Topic_name varchar(100) character set utf8,
                Topic_link varchar(100) character set utf8
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
                News_id int,
                Topic_id int
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
                Author_id int primary key,
                Author_name varchar(100) character set utf8,
                Author_link varchar(100) character set utf8
            ); """
    cursor.execute(sql)

#--------------------------------------main function-----------------------------------------
json_directory = sys.argv[1]
database_name = sys.argv[2]
news_source = sys.argv[3]
print(json_directory+" "+database_name+" "+news_source)
news_json_to_sql(json_directory,database_name,news_source)