from scmagazine_crawler import scmagazine_crawler
import json
sc = scmagazine_crawler()
#url = 'https://www.scmagazine.com/open-aws-s3-bucket-managed-by-walmart-jewelry-partner-exposes-info-on-13m-customers/article/751751/'
#url = 'https://www.scmagazine.com/'
news_list = sc.get_all_news_list('cybercrime/navigations.txt')
with open("cybercrime/news_list.json","w") as f:
   json.dump(news_list, f)
news_list = sc.get_all_news_list('network security/navigations.txt')
with open("network security/news_list.json","w") as f:
   json.dump(news_list, f)
with open("cybercrime/news_list.json","r") as f:
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

