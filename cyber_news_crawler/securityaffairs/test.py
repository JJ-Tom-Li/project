from securityaffairs_crawler import securityaffairs_crawler
import json
sc = securityaffairs_crawler()
news_list = sc.get_all_news_list("news/navigations2.txt")
with open("news_list2.json","w") as f:
   json.dump(news_list, f)
start_flag = False    #Start to crawl news if the flag is true
with open("news_list2.json","r") as f:
    #Read the news names and links from file.
    news_list = json.load(f)
    for navi in news_list:
        if(navi['navigation']=='Intelligence'):
            #Start crawl if the navigaion is what we want.
            start_flag=True
        if(not start_flag):
            continue    
        
        #Copy the content of navi(aka the news names and link of this navigaion) to navi_tmp.
        navi_tmp = navi
        print("Navi:"+navi['navigation'])
        
        #Crawl news one by one.
        for index,news in enumerate(navi_tmp['news_list']):
            print("Crawl the ",index,"th news:"+news['news_name'])
            #Skip if the news name or link is blank.
            if len(news) >2:
                continue
            tmp = sc.crawler(news['news_link'])
            #Put the web content into news list
            news.update(tmp)
        #Dump the news list into json file.
        with open("news/"+navi['navigation']+".json","w") as f:
            json.dump([navi_tmp], f)

            