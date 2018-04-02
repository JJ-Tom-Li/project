# news/  
	存放爬下來的新聞json檔，news_list2.json有全部的新聞名稱及連結  
# `Class securityaffairs_cralwer`  
	
**`def get_all_news_list(self,filename):`** 讀取一個有新聞navigaition連結與名稱的txt檔，取得該navagaion下全部的新聞名稱及連結，輸出成json檔。txt檔的格式如news/navagation.txt。  
**`def crawler(self,url):`** 將url(網址)指定的網頁爬取下來，輸出成如下格式:  
	{
		'title':title,			#title:string
		'author':author[0],		#author:string
		'author_link':author[1],#author_link:string
		'date':date,			#date:string
		'body':body,			#body:string
		'topics':topics			#topics:list of dict{'topic_link':string,'topic_name':string}
	} 
**`def get_title(self,soup):`**  
**`def get_author(self,soup):`**  
**`def get_date(self,soup):`**  
**`def get_body(self,soup):`**  
**`def get_topics(self,soup):`**  
