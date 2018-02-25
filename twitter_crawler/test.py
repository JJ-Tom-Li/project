from twitter_crawler import Twitter_crawler
import pickle
with open("keys.txt","r") as f:
	tmplist = f.read().split('\n')
	consumer_key = tmplist[0] 
	consumer_secret = tmplist[1]  
	access_token = tmplist[2]  
	access_token_secret = tmplist[3]
tc = Twitter_crawler(consumer_key,consumer_secret,access_token,access_token_secret)
tc.crawler("output.json","CVEnew",1,1)
tc.print_json("output.json")