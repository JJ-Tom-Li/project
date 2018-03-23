import requests
import json
import pyprind
from bs4 import BeautifulSoup
from collections import OrderedDict
import threading
class scmagazine_crawler:
	#def __init__(self):
		
	def crawler(self,url):
		#The url of website
		
		#get the contain of website
		res = requests.get(url)
		soup = BeautifulSoup(res.text,"lxml")
		
		#取得文章標題
		title = self.get_title(soup)
		#取得文章作者
		author = self.get_author(soup)
		#取得文章發表日期
		date = self.get_date(soup)
		#取得文章本身
		body = self.get_body(soup)
		#取得文章主題類別
		topics = self.get_topics(soup)
		
		return {
					'title':title,			#title:string
					'author':author[0],		#author:string
					'author_link':author[1],#author_link:string
					'date':date,			#date:string
					'body':body,			#body:string
					'topics':topics			#topics:list of dict{'topic_link':string,'topic_name':string}
				}
	def get_title(self,soup):	
		return soup.find('article').find('h1').text
	
	def get_author(self,soup):
		author = soup.select('div[class="author-name"]')
		author_name = author[0].find('a')['title']
		author_link = author[0].find('a')['href']
		return (author_name,author_link)
	
	def get_date(self,soup):
		return soup.find('article').find('time').text
	
	def get_body(self,soup):
		article_body = soup.select('div[class="article-body"]')[0].find_all('p')
		body_text = ''
		for p in article_body:
			body_text+=p.text+"\n\n"
		return body_text
	
	def get_topics(self,soup):
		topic_a = soup.find('section', attrs={'class':'flexibleTagsTags artTags'}).find_all('a')
		topics = []
		for t in topic_a:
			topics.append({'topic_link':t['href'],'topic_name':t.text})
		return topics
