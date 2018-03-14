import tweepy
import json
import time
class Twitter_crawler:
	def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret,a=1):
		self.consumer_key=consumer_key
		self.consumer_secret=consumer_secret
		self.access_token=access_token
		self.access_token_secret=access_token_secret
		#創建認證
		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)  
		# 設置access token和access secret
		self.auth.set_access_token(self.access_token, self.access_token_secret)  
		# create API and make it into json serailizable
		self.api = tweepy.API(self.auth,parser=tweepy.parsers.JSONParser())  

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
				for index,j in enumerate(results):
					dataout.append(j)
				print("Page " + str(i) + " finished.")
			jsonf.write(json.dumps(dataout))
	def crawler_by_time(self,outputjson,twitter_name,start_time,end_time):
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
				for index,j in enumerate(results):
					dataout.append(j)
				print("Page " + str(i) + " finished.")
			jsonf.write(json.dumps(dataout))
	def print_cve_json(self,filename):
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
	def get_user(self,username):
		user = self.api.get_user(username)
		return user
	def user_to_json(self,user):
		j = json.dumps(user,ensure_ascii=False)
		return j
	'''	
	def get_followers(self,twitter_name):
		follower_id = []
		dataout=[]
		index=0
		api = tweepy.API(self.auth, wait_on_rate_limit=True
						 , wait_on_rate_limit_notify=True, compression=True)

		api = tweepy.API(self.auth, compression=True)
		real_number = 0

		for page in tweepy.Cursor(api.followers,screen_name=twitter_name).pages():

				index = index + 1
				real_number  = real_number + len(page)
				for item in page:
					if(item.followers_count<1000):
						page.remove(item)
				follower_id.extend(page)
				print("real:"+str(real_number))
				print(len(follower_id))
			for follower in follower_id:
				print(follower)

		with open("followers2","w") as f:
			index = 0
			key = 1
			for uid in follower_id:
				index = index + 1
				try:
					user = api.get_user(uid)
					if(user.followers_count>=100):
						print(str(index)+":"+user.screen_name)
					f.write(user.screen_name+"\n")
				except:
					print("change keys")
					key = key + 1
					filename = "keys/keys"+str(key)+".txt"
					self.get_keys(filename)
					api = tweepy.API(self.auth, compression=True)
	'''
	def get_keys(self,filename):
		with open(filename,"r") as f:
			tmplist = f.read().split('\n')
			consumer_key = tmplist[0] 
			consumer_secret = tmplist[1]  
			access_token = tmplist[2]  
			access_token_secret = tmplist[3]
		self.__init__(consumer_key,consumer_secret,access_token,access_token_secret)