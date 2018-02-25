import tweepy
import json
class Twitter_crawler:
	consumer_key=""
	consumer_secret=""
	access_token=""
	access_token_secret=""
	def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
		self.consumer_key=consumer_key
		self.consumer_secret=consumer_secret
		self.access_token=access_token
		self.access_token_secret=access_token_secret
		#創建認證
		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)  
		# 設置access token和access secret
		auth.set_access_token(self.access_token, self.access_token_secret)  
		# create API and make it into json serailizable
		self.api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())  

	def crawler(self,outputjson,twitter_name,start_page,max_page):
		
		# Twitter target
		name = twitter_name

		# number of tweets
		number=1;
		
		dataout=[]
		# crawl	
		print("@"+name+":start crawl:")
		with open(outputjson,"w") as jsonf:
			for i in range(start_page,max_page+1):
					# user user_timeline() to crawl tweet
				results = self.api.user_timeline(id=name, page=i,tweet_mode='extended')
				#while(len(results)>0):
					#load data from result list

				for index,j in enumerate(results):
					
					dataout.append(j)

				print("Page " + str(i) + " finished.")
				
			jsonf.write(json.dumps(dataout))
			
	def print_json(self,filename):
		inputdata=[]
		with open(filename, encoding='utf-8') as f:
			inputdata=json.loads(f.read())
			inputdata = sorted(inputdata, key=lambda k: k.get('created_at', 0), reverse=True)
			for index,i in enumerate(inputdata):
				print("The "+str(index+1)+" exploits:\n")
				print("\t"+i['full_text'].split(' ')[0])
				print("\t****************************************************************************") 
				print("\t"+' '.join(i['full_text'].split(' ')[1:]))
				print("\t****************************************************************************") 
				
				print("\tCreated at:"+i['created_at'] )
				print("\tURL:"+i['entities']['urls'][0]['expanded_url']+"\n")
				
				
				
				
				
				
				