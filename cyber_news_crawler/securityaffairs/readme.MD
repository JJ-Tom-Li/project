# news/  
	存放爬下來的新聞json檔，news_list2.json有全部的新聞名稱及連結  
# `Class securityaffairs_cralwer`  
	
**`def get_all_news_list(self,filename):`** 讀取一個有新聞navigaition連結與名稱的txt檔，取得該navagaion下全部的新聞名稱及連結，輸出成json檔。txt檔的格式如news/navagation.txt。  
**`def crawler(self,url):`** 將url(網址)指定的網頁爬取下來，輸出成如下格式:  
```   
{
	'title':title,			#title:string
	'author':author[0],		#author:string
	'author_link':author[1],#author_link:string
	'date':date,			#date:string
	'body':body,			#body:string
	'topics':topics			#topics:list of dict{'topic_link':string,'topic_name':string}
}
```  
**`def get_title(self,soup):`** 取得soup中的新聞標題，return一個string。   
**`def get_author(self,soup):`** 取得soup中的新聞作者，return一個tuple`(author_name::string,author_link::string)`。  
**`def get_date(self,soup):`** 取得新聞的發布日期，return一個string。   
**`def get_body(self,soup):`** 取得新聞的文章內容，return一個string。   
**`def get_topics(self,soup):`** 取得新聞的相關關鍵字，return一個list`[{topic_name::string,topic_link::string}]`。  

# test.py 使用方法  
## 1.爬取全部新聞的標題與連結  
首先修改`news_list = sc.get_all_news_list("news/navigations2.txt")`這行後面的檔名，此檔名為預先查詢的navigation名稱及連結，可使用news中的navigaion2.txt。  

## 2.將新聞連結與名稱輸出成json檔案  
```  
with open("news_list2.json","w") as f:
   json.dump(news_list, f)
```  
這行會開啟一個news_list2.json檔案，將步驟1return的news_list object輸出成json file.  

## 3.爬取全部新聞  
`with open("news_list2.json","r") as f:`這行會開啟news_list2.json檔案讀取新聞名稱及連結。  
`if(navi['navigation']=='Intelligence'):` 這行可以設定要從哪個navigaion開始爬取新聞。    
`with open("news/"+navi['navigation']+".json","w") as f:` 這行可以決定輸出的檔案名稱，預設是navigation_name.json  


