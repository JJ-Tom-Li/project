from securityaffairs_crawler import securityaffairs_crawler

sc = securityaffairs_crawler()
url = 'http://securityaffairs.co/wordpress/61750/hacking/solar-panels-flaws.html'
print(sc.crawler(url))