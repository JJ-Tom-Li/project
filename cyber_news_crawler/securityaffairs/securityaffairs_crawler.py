import requests
import json
import re
from bs4 import BeautifulSoup
from collections import OrderedDict
import threading
class securityaffairs_crawler:
	#def __init__(self):
	'''
	def get_all_news_categories(self):
		url = 'http://securityaffairs.co/wordpress/'
		#get the contain of website
		res = requests.get(url)
		soup = BeautifulSoup(res.text,"lxml")

		news_cate = soup.find('ul',attrs={'class','second_nav'}).find_all('li')
		for cate in news_cate:
			print(cate.find('a')['href']+" "+cate.find('a').text)
	'''
	def get_all_news_list(self,filename):
		with open(filename,"r") as f:
			#read navigations' names and links from file
			navis = f.read().split('\n')
			navis_list = []
			for n in navis:
				if n=="" or n=="\n":
					break
				n=n.split()
				#store to list
				navis_list.append((n[1],n[0])) 
			for n in navis_list:
				print(n[0]," ",n[1])
			
			news_list=[]
			for navi in navis_list:
				#get the list of news_name and news_link from navigation
				print("Get news from "+navi[0]+":")

				res = requests.get(navi[1])
				soup = BeautifulSoup(res.text,"lxml")
				#Get the number of last page
				last_page = [page for page in soup.select('div[class="pagination"]')[0]
													.find_all('a') if page.text=="Last »"]
				last_page = last_page[0]['href']
				last_page = int(last_page[last_page.find('page')+len('/page'):])
				
				#Create the dict form of news
				tmp = {'navigation':navi[0],'news_list':[]}
				#Crawl the news page by page
				for i in range(1,last_page+1):
					print(navi[0]+":page ",i)
					res = requests.get(navi[1]+"/page/"+str(i))
					soup = BeautifulSoup(res.text,"lxml")
					try:
						#Get the row of news
						news_row = soup.find('div',attrs={'class',"sidebar_content"}).find_all('div',id=re.compile('^post-'))
						
						for news in news_row:
							#Get the news name and link row by row
							tmp['news_list'].append({'news_name':news.find('h3').find('a')['title'],
														'news_link':news.find('h3').find('a')['href']})
					except:
						continue
				#put into news_list list
				news_list.append(tmp)
					
		return news_list
		
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
		try:	
			return soup.select('div[class="post_header_wrapper"]')[0].find('h1',attrs={'class','post_title'}).text.lstrip()
		except:
			return ""
	def get_author(self,soup):
		try:
			author = soup.select('div[class="post_detail"]')
			author_name = author[0].find('a').text.replace('\xa0',' ')
			author_link = author[0].find('a')['href']
			return (author_name,author_link)
		except:
			return ("","")
	def get_date(self,soup):
		try:
			date = soup.select('div[class="post_detail"]')[0].text.strip()
			#delete the 'By'
			return date[:date.find('By')].strip()
		except:
			return ""
	
	def get_body(self,soup):
		try:
			article_body = soup.select('div[class="post_inner_wrapper"]')[0].find_all('p')
			body_text = ''
			for p in article_body:
				body_text+=p.text.replace('\xa0',' ')+"\n\n"
			return body_text
		except:
			return ""
	
	def get_topics(self,soup):
		try:
			topic_a = soup.select('div[class="post_tag"]')[0].find_all('a')
			topics = []
			for t in topic_a:
				topics.append({'topic_link':t['href'],'topic_name':t.text})
			return topics
		except:
			return ""
