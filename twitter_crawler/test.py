from twitter_crawler import Twitter_crawler
import json
import time
#get the keys
with open("keys/keys2.txt","r") as f:
	tmplist = f.read().split('\n')
	consumer_key = tmplist[0] 
	consumer_secret = tmplist[1]  
	access_token = tmplist[2]  
	access_token_secret = tmplist[3]
#宣告Twitter_crawler物件
tc = Twitter_crawler(consumer_key,consumer_secret,access_token,access_token_secret)
#取得所有的專家user資料
#tc.get_users("experts/horus_experts.txt")	
#tc.crawler_by_time("output_by_time.json","Polder_PV")
tc.print_tweets("output_by_time.json")
#tc.print_user_by_followers("experts/horus_experts.json")