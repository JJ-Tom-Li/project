from scmagazine_crawler import scmagazine_crawler

sc = scmagazine_crawler()
url = 'https://www.scmagazine.com/open-aws-s3-bucket-managed-by-walmart-jewelry-partner-exposes-info-on-13m-customers/article/751751/'
print(sc.crawler(url))