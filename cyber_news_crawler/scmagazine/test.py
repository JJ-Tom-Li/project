from scmagazine_crawler import scmagazine_crawler
import json
sc = scmagazine_crawler()
#url = 'https://www.scmagazine.com/open-aws-s3-bucket-managed-by-walmart-jewelry-partner-exposes-info-on-13m-customers/article/751751/'
url = 'https://www.scmagazine.com/'
news_list = sc.get_all_news_list('cybercrime/navigations.txt')
with open("testfile.json","w") as f:
    json.dump(news_list, f)