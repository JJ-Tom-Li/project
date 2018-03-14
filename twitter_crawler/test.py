from twitter_crawler import Twitter_crawler
import pickle
import json
with open("keys/keys2.txt","r") as f:
	tmplist = f.read().split('\n')
	consumer_key = tmplist[0] 
	consumer_secret = tmplist[1]  
	access_token = tmplist[2]  
	access_token_secret = tmplist[3]
	
tc = Twitter_crawler(consumer_key,consumer_secret,access_token,access_token_secret)

with open("experts/horus_experts.txt","r") as inputf:
	try:
		names = []
		old_data = []
		with open("experts/horus_experts.json",encoding='utf-8') as jsonf:
			try:
				old_data = json.loads(jsonf.read())
				for expert in old_data:
					names.append(expert['screen_name'])
			except json.decoder.JSONDecodeError :
				print("Json file error.")
	except FileNotFoundError:
		print("Json file is not found.Create new one.")
			
	with open("experts/horus_experts.json","w") as jsonf:
		outputjson=[]
		if len(names)!=0:
			for name in names:
				print(name)
			outputjson.extend(old_data)
		experts_name = inputf.read().split('\n')
		for expert in experts_name:
			if expert == "" :
				#blank name
				continue
			if expert in names:
				print(expert+" is already in file.")
				continue
			user = tc.get_user(expert)
			outputjson.append(user)
			print("Expert \""+expert+"\" done.")
		jsonf.write(json.dumps(outputjson))
		
#tc.crawler("output.json","CVEnew",1,1)
#tc.print_json("output.json")
#tc.get_followers("Cvenew")
#tc.search()