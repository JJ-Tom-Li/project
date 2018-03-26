from securityaffairs_crawler import securityaffairs_crawler
import json
sc = securityaffairs_crawler()
url = 'http://securityaffairs.co/wordpress/61750/hacking/solar-panels-flaws.html'
#print(sc.crawler(url))
news_list = sc.get_all_news_list("news/navigations2.txt")
with open("news_list.json","w") as f:
   json.dump(news_list, f)
'''
with open("news/news_list.json","r") as f:
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
        with open("news/"+navi['navigation']+".json","w") as f:
            json.dump([navi_tmp], f)
            '''