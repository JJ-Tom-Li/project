import requests
import json
import pyprind
from bs4 import BeautifulSoup
from collections import OrderedDict
import threading
from selenium import webdriver

dataout = []
def crawler(url,start_page,end_page):
	with open("output.json","w") as f:
		#開瀏覽器
		browser = webdriver.Firefox()
		#取得網址
		browser.get(url)
		#取得"產品總覽"超連結
		res = browser.find_element_by_id('ContentPlaceHolder1_LinkButton11')
		#點下去
		res.click()	 
		#crawl from start_page to end_page
		for i in pyprind.prog_bar(range(start_page,end_page+1)):
			#排除掉第一頁
			if(i!=1): 
				#找到下一頁的按鈕
				res = browser.find_element_by_link_text(str(i))
				#按下去
				res.click()
			#get the source of page
			pagesource = browser.page_source
			#get the contain of website
			soup = BeautifulSoup(pagesource,"lxml")
			#get the table
			table = soup.find('table', attrs={'id':'ContentPlaceHolder1_GVTABPRO'})
			#get the rows of table
			rows = table.find_all('tr')
			index = 0
			for row in rows:
				#index == 1 means it's the first col 
				if (index == 0):
					cols = row.find_all('th')
					colname = [element.text.strip() for element in cols]
					index = index + 1
				else:
					#get the cols from rows
					cols = row.find_all('td')
					#the elements of table is stored in cols now
					cols = [element.text.strip() for element in cols]
					#the row of pages
					if(cols[0]=='12345678910'):
						break
					#store the cols into data
					#data is the type of dict
					data = {	str(colname[0]):cols[0],
								str(colname[1]):cols[1],
								str(colname[2]):cols[2],
								str(colname[3]):cols[3],
								str(colname[4]):cols[4],
								str(colname[5]):cols[5],
								str(colname[6]):cols[6],
								str(colname[7]):cols[7],
								str(colname[8]):cols[8]
						   }
					#store into dataout
					dataout.append(data)
		browser.close()
		f.write(json.dumps(dataout))
		
crawler("https://pvipl.itri.org.tw/t1.aspx",1,10)

