import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import json
class PageStart:
	def spidering(self,url):
		res = requests.get(url, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		title = self.get_title(soup)
		authur = self.get_authur(soup)
		date = self.get_date(soup)
		body = self.get_body(soup)
		tag = self.get_tag(soup)

		'''
		print(title)
		print(authur)
		print(date)
		print(body)
		print(tag)
	'''

		
		return {
					'title':title,
					'authur':authur,
					'date':date,
					'body':body,
					'topics':tag
				}
		

	def get_title(self,soup):
		try:
			article_title = soup.find('h1',attrs={'class':'entry-title'})
			article_title = article_title.text.strip()
			return article_title
		except:
			return ""

	def get_authur(self,soup):
		try:
			authur = soup.find('a',attrs={'class':'url fn n'})
			authur = authur.text.strip()
			return authur
		except:
			return ""
		
	def get_date(self,soup):
		try:
			article_date = soup.find('time',attrs={'class':'entry-date published'})
			article_date = article_date.text.strip()
			return article_date
		except :
			return ""
	def get_body(self,soup):
		try:
			article_body = soup.find('div',attrs={"class",'theiaPostSlider_preloadedSlide'}).find_all('p')
			body_text = ''
			for p in article_body:
				body_text += p.text 
			#body_text = body_text.encode('utf-8')
			body_text = body_text.replace(u'\xa0',u' ')
			#body_text = body_text.replace(u'\xe2\x80\x9c',u'"')
			#body_text = body_text.replace(u'\xe2\x80\x9d',u'"')
			return body_text#.encode()
		except:
			return ""
		
	def get_tag(self,soup):	
		try:
			related_tag = soup.find('div',attrs={"class",'src'}).find_all('a')
			tags =[]
			for a in related_tag:
				tags.append(a.text)
			return tags
		except:
			return ""