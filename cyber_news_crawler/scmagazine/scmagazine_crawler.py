import requests
import json
from bs4 import BeautifulSoup
from collections import OrderedDict
import threading
class scmagazine_crawler:
	#def __init__(self):
	def get_all_news_list(self,filename):
		with open(filename,"r") as f:
			#read navigations' names and links from file
			navis = f.read().split('\n')
			navis_list = []
			for n in navis:
				if n=="" or n=="\n":
					break
				n=n.split()
				#get the html of n[0]
				res = requests.get(n[0])
				soup = BeautifulSoup(res.text,"lxml")
				#turn the link into all_news link
				n[0]=soup.find('a',attrs={'class',"see-all-btn next colr-red"})['href']
				
				#store to list
				navis_list.append((n[1],n[0])) 
			news_list=[]
			for navi in navis_list:
				#get the list of news_name and news_link from navigation
				print("Get news from "+navi[0]+":")

				res = requests.get(navi[1])
				soup = BeautifulSoup(res.text,"lxml")
				#Get the row of news
				news_row = soup.find('div',attrs={'class',"row-list"}).find_all('div',attrs={'class',"row"})
				#Create the dict form of news
				tmp = {'navigation':navi[0],'news_list':[]}
				for news in news_row:
					#Get the news name and link row by row
					tmp['news_list'].append({'news_name':news.find('h2').find('a')['title'],
												'news_link':news.find('h2').find('a')['href']})
				#put into news_list list
				news_list.append(tmp)
		return news_list
	def news_list_crawler(self,news_list):
		for news in news_list:
			print("Crawl the '"+news['news_name']+"' news.")
			res = requests.get(news['news_link'])
			soup = BeautifulSoup(res.text,"lxml")
			
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
			return soup.find('article').find('h1').text
		except:
			return ""
	
	def get_author(self,soup):
		try:
			#get the author data
			author = soup.select('div[class="author-name"]')
			#get the author name from title
			author_name = author[0].find('a')['title']
			#get the author link from href
			author_link = author[0].find('a')['href']
			return (author_name,author_link)
		except:
			return ("","")
	
	def get_date(self,soup):
		try:
			#get the date from article
			return soup.find('article').find('time').text
		except:
			return ""

	def get_body(self,soup):
		try:
			#get the article body
			article_body = soup.select('div[class="article-body"]')[0].find_all('p')
			body_text = ''
			#combine the text of article body
			for p in article_body:
				body_text+=p.text+"\n\n"
			return body_text
		except:
			return ""

	def get_topics(self,soup):
		try:
			#get topics from tags
			topic_a = soup.find('section', attrs={'class':'flexibleTagsTags artTags'}).find_all('a')
			topics = []
			#put topics into list
			for t in topic_a:
				topics.append({'topic_link':t['href'],'topic_name':t.text})
			return topics
		except:
			return []
