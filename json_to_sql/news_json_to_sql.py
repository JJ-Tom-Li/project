import json
import pymysql
import getpass
import sys
import datetime
import re
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
            try:
                jsondata = jsondata[0]
                navigation = jsondata['navigation']
            except:
                #if There is no navigation
                print("Navigation is not found.Continue next step.")

            #json data to sql format
            print("\tInsert data to table...")

            #Get the last id of tables
            newsid_count = get_last_id_of_table(cursor,"News_header")+1
            authorid_count = get_last_id_of_table(cursor,"News_author")+1
            topicid_count = get_last_id_of_table(cursor,"News_topic")+1

            for item in jsondata['news_list']:
                #避免重複
                if get_news_id(cursor,item['title']) ==0:
                    #print(item['title'])
                    #Parsing the author id
                    tmpid = get_author_id(cursor,item['author'])
                    if tmpid!=0:
                        #The author has been store in table.
                        authorid = tmpid
                    else:
                        #Author not be found in table.Create a new author information.
                        authorid = authorid_count
                        authorid_count = authorid_count + 1

                        #Insert News_author
                        sql = """insert into News_author(Author_id,Author_name,Author_link)
                                values (%s,%s,%s);
                            """
                        cursor.execute(sql,(authorid,
                                            item['author'],
                                            item['author_link']
                                            ))

                    #Insert News_header
                    sql = """insert into News_header(News_id,Title,Date,author_id,News_source)
                            values (%s,%s,%s,%s,%s);
                        """
                    cursor.execute(sql,(newsid_count,
                                        item['title'],
                                        date_to_datetime(item['date']),
                                        authorid,
                                        news_source
                                        ))
                    
                    #Insert News_content
                    sql = """insert into News_content(News_id,News_link,News_body)
                            values (%s,%s,%s);
                        """
                    cursor.execute(sql,(newsid_count,
                                        item['news_link'],
                                        remove_non_ascii(item['body'])
                                        ))
                            
                    #Insert News_topic and News_to_topic
                    for t in item['topics']:
                        #Parsing the topic id
                        tmpid = get_topic_id(cursor,t['topic_name'])
                        if tmpid!=0:
                            #The topic has been stored in table.
                            topicid = tmpid
                        else:
                            #Author not be found in table.Create a new author information.
                            topicid = topicid_count
                            topicid_count = topicid_count + 1

                            #Insert into News_topic table
                            sql = """insert into News_topic(Topic_id,Topic_name,Topic_link)
                                values (%s,%s,%s);
                            """
                            cursor.execute(sql,(topicid,
                                            t['topic_name'],
                                            t['topic_link']
                                            ))
                        #Insert News_to_topic
                        sql = """insert into News_to_topic(News_id,Topic_id)
                                values (%s,%s);
                            """
                        cursor.execute(sql,(newsid_count,
                                            topicid
                                            ))
                     
                    

                    
                    newsid_count = newsid_count + 1
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
    sql = "select topic_id from News_topic where topic_name=%s;"
    cursor.execute(sql,topic)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0
    return 0
def date_to_datetime(date):
    import time
    if date=="":
        return None
    else:
        t = time.strptime(date, "%B %d, %Y")
        return t
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
                News_body text character set utf8mb4
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
                Topic_id int primary key,
                Topic_name varchar(100) character set utf8,
                Topic_link varchar(200) character set utf8
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
emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)

def remove_emoji(text):
    return emoji_pattern.sub(r'', text)
from unicodedata import normalize
def remove_non_ascii(text):
    return normalize('NFKD', text).encode('ascii','ignore')
#--------------------------------------main function-----------------------------------------
json_directory = sys.argv[1]
database_name = sys.argv[2]
news_source = sys.argv[3]
print(json_directory+" "+database_name+" "+news_source)
news_json_to_sql(json_directory,database_name,news_source)