# -*- coding: utf-8 -*-
from nltk_parser import *
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer
import pymysql
import getpass
import sys

"""
    This program will export keywords of news to MySQL database.
    Usage: python test.py [database_name] [number_of_keywords_per_news]
"""
def number_of_news(cursor):
    count=0
    sql = "select count(*) from news_header"
    cursor.execute(sql)

    return int(cursor.fetchone()[0])
def read_text_token_list_from_file(filename):
    import pickle
    try:
        with open(filename,"rb") as f:
            text_token = pickle.load(f)
            return text_token
    except:
        return []
def write_text_token_list_to_file(filename,text_token):
    import pickle
    with open(filename,"wb") as f:
        pickle.dump(text_token,f)
def create_keyword_tables(cursor):
    sql = """create table if not exists news_to_keyword(
                    News_id int,
                    keyword_id int,
                    Keyword_tfidf double
        );"""
    cursor.execute(sql)
    sql = """create table if not exists news_keyword(
            Keyword_id int primary key,
            Keyword_name varchar(100) character set utf8
        );"""
    cursor.execute(sql)

def get_keyword_id(cursor,keyword_name):
    sql = "select keyword_id from news_keyword where keyword_name=%s"
    cursor.execute(sql,keyword_name)
    result = cursor.fetchone()

    if result:
        return int(result[0])
    else:
        return 0
def get_last_keyword_id(cursor):
    sql = "select count(*) from news_keyword"
    cursor.execute(sql)
    result = cursor.fetchone()

    return int(result[0])
def news_keyword(database_name,number_of_keywords_per_news):
    #Get the username and password of database
    username=""
    password=""
    username = input("Please enter local database Username:")
    password = getpass.getpass("Local database Password:")
    #Try to connect to the database
    try:
        print("Connect to database "+database_name+"...")
        db = pymysql.connect("localhost",username,password,database_name,use_unicode=True, charset="utf8")
    except:
        print("Error while connecting database.")
        return
    
    #Create mysql cursor and some objects
    cursor = db.cursor()
    nltk_parser = NLTK_parser()
    all_text_word_token = []

    #count the number of news
    number = number_of_news(cursor)

    #read the former text tokens from file
    all_text_word_token = read_text_token_list_from_file("news_text_word_token.txt")

    #compare the number of all_text_word_token to number_of_news
    if len(all_text_word_token) != number:
        #Create new all_text_word_token if the number is different.
        print("The text_word_token file is out of date or missing.Create a news one.")

        sql ="select news_id,news_body from news_content;"

        #get the news contents
        cursor.execute(sql)
        result = cursor.fetchall()
        
        index = 1

        print("tokening news:")
        for id_and_text in result:
            
            token = nltk_parser.get_text_word_token(id_and_text[1])
            all_text_word_token.append(token)
            index = index +1
        write_text_token_list_to_file("news_text_word_token.txt",all_text_word_token)

    #Create the keyword tables;    
    create_keyword_tables(cursor)

    #Counting the keyword id
    keywordid_count = get_last_keyword_id(cursor)

    for i in range(1,number+1):
        sql = "select title from news_header where news_id=%s;"
        cursor.execute(sql,i)
        result = cursor.fetchone()
        print("\nThe ",i,"th News")
        
        sql = "select count(*) from news_to_keyword where news_id=%s"
        cursor.execute(sql,i)
        result = cursor.fetchone()[0]
        if result==20:
            continue
        else:
            #Get keywords
            keywords = nltk_parser.find_keywords(all_text_word_token,i,number_of_keywords_per_news)
        for j,word in enumerate(keywords):
            if j<result:
                continue
            keywordid = get_keyword_id(cursor,word[0])
            #There is no the keyword
            if keywordid == 0:
                keywordid_count = keywordid_count + 1
                keywordid = keywordid_count

                if len(word[0])>100:
                    try:
                        word[0]=word[0][100:]
                    except:
                        word[0]=""
                sql = "Insert into news_keyword(keyword_id,keyword_name) values(%s,%s)"
                cursor.execute(sql,(keywordid,word[0]))

            sql = "Insert into news_to_keyword(news_id,keyword_id,keyword_tfidf) values(%s,%s,%s)"
            #insert news_id,keyword_id and keyword_tfidf into table 
            cursor.execute(sql,(i,keywordid,float(word[1])))
            db.commit()
    
    db.close() 
#nltk_parser.parser(dir="news/horus scenario/",outfile="",number_of_result=50)
#nltk_parser.show_tag_of_words('NN')
#nltk_parser.keywords("news/test/")
database_name=sys.argv[1]
number_of_keywords_per_news=sys.argv[2]
news_keyword(database_name,int(number_of_keywords_per_news))