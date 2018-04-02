from scmagazine_crawler import scmagazine_crawler
import json

sc = scmagazine_crawler()

#Get the news list of cybercrime
news_list = sc.get_all_news_list('cybercrime/navigations.txt')
#output news_list to news_list.json
with open("cybercrime/news_list.json","w") as f:
   json.dump(news_list, f)

#Get the news list of cybercrime
news_list = sc.get_all_news_list('network security/navigations.txt')
#output news_list to news_list.json
with open("network security/news_list.json","w") as f:
   json.dump(news_list, f)

#Read the news list from news_list file
with open("cybercrime/news_list.json","r") as f:
    news_list = json.load(f)

    for navi in news_list:
        navi_tmp = navi #Copy
        print("Navi:"+navi['navigation'])

        #Crawl the news one by one
        for index,news in enumerate(navi_tmp['news_list']):
            print("Crawl the ",index,"th news:"+news['news_name'])
            #Skip if the news is crawled.(?)
            if len(news) >2:
                continue
            
            tmp = sc.crawler(news['news_link'])
            news.update(tmp)
        #Output to file.
        with open("cybercrime/"+navi['navigation']+".json","w") as f:
            json.dump([navi_tmp], f)

with open("network security/news_list.json","r") as f:
    news_list = json.load(f)
    for navi in news_list:
        navi_tmp = navi
        print("Navi:"+navi['navigation'])
        for index,news in enumerate(navi_tmp['news_list']):
            print("Crawl the ",index,"th news:"+news['news_name'])
            if len(news) >2:
                continue
            tmp = sc.crawler(news['news_link'])
            news.update(tmp)
        with open("network security/"+navi['navigation']+".json","w") as f:
            json.dump([navi_tmp], f)     
#with open("testfile.json","w") as f:
#    json.dump(news_list, f)

