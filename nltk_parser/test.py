from nltk_parser import *
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer
import pymysql
import getpass
def news_keyword(database_name,news_id):
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
    sql ="select news_id,news_body from news_content;"
    cursor.execute(sql)
    result = cursor.fetchall()
    nltk_parser = NLTK_parser()
    all_text_word_token = []
    index = 1
    for id_and_text in result:
        print("tokening the "+str(index)+"th news:")
        token = nltk_parser.get_text_word_token(id_and_text[1])
        all_text_word_token.append(token)
        index = index +1
    nltk_parser.find_keywords(all_text_word_token,news_id)
#nltk_parser.parser(dir="news/horus scenario/",outfile="",number_of_result=50)
#nltk_parser.show_tag_of_words('NN')
#nltk_parser.keywords("news/test/")
news_keyword("sis",4532)