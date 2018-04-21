import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from page import page
import json
import codecs
import time

LHN = page()



FirstPage = 'https://latesthackingnews.com/category/hackingnews/'
data = []
page = []

'''
for j in range(11):
	if j == 0:
		continue
	elif j == 1:
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find_all('div',attrs={"class",'entry-content clearfix'})
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			#print(i)
			data.append(LHN.spidering(i))
			time.sleep(3)
		page.clear()
	else:
		FirstPage = 'https://latesthackingnews.com/category/hackingnews/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find_all('div',attrs={"class",'entry-content clearfix'})
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			#print(i)
			data.append(LHN.spidering(i))
			time.sleep(3)
		page.clear()
with open('LHNdata_1_10.json', 'w') as f:
		json.dump(data, f)
data.clear()
'''
'''
for j in range(21):
	if j < 11:
		continue
	else:
		FirstPage = 'https://latesthackingnews.com/category/hackingnews/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find_all('div',attrs={"class",'entry-content clearfix'})
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			#print(i)
			data.append(LHN.spidering(i))
			time.sleep(3)
		page.clear()
with open('LHNdata_11_20.json', 'w') as f:
		json.dump(data, f)
data.clear()
'''
'''
for j in range(31):
	if j < 21:
		continue
	else:
		FirstPage = 'https://latesthackingnews.com/category/hackingnews/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find_all('div',attrs={"class",'entry-content clearfix'})
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			#print(i)
			data.append(LHN.spidering(i))
			time.sleep(2)
		page.clear()
with open('LHNdata_21_30.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(41):
	if j < 31:
		continue
	else:
		FirstPage = 'https://latesthackingnews.com/category/hackingnews/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find_all('div',attrs={"class",'entry-content clearfix'})
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			#print(i)
			data.append(LHN.spidering(i))
			time.sleep(2)
		page.clear()
with open('LHNdata_31_40.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(51):
	if j < 41:
		continue
	else:
		FirstPage = 'https://latesthackingnews.com/category/hackingnews/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find_all('div',attrs={"class",'entry-content clearfix'})
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			#print(i)
			data.append(LHN.spidering(i))
			time.sleep(2)
		page.clear()
with open('LHNdata_41_50.json', 'w') as f:
		json.dump(data, f)
data.clear()
'''
'''
for j in range(61):
	if j < 51:
		continue
	else:
		FirstPage = 'https://latesthackingnews.com/category/hackingnews/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find_all('div',attrs={"class",'entry-content clearfix'})
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			#print(i)
			data.append(LHN.spidering(i))
			time.sleep(2)
		page.clear()
with open('LHNdata_51_60.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(71):
	if j < 61:
		continue
	else:
		FirstPage = 'https://latesthackingnews.com/category/hackingnews/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find_all('div',attrs={"class",'entry-content clearfix'})
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			#print(i)
			data.append(LHN.spidering(i))
			time.sleep(2)
		page.clear()
with open('LHNdata_61_70.json', 'w') as f:
		json.dump(data, f)
data.clear()



for j in range(81):
	if j < 71:
		continue
	else:
		FirstPage = 'https://latesthackingnews.com/category/hackingnews/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find_all('div',attrs={"class",'entry-content clearfix'})
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			#print(i)
			data.append(LHN.spidering(i))
			time.sleep(2)
		page.clear()
with open('LHNdata_71_80.json', 'w') as f:
		json.dump(data, f)
data.clear()
'''
'''
for j in range(101):
	if j < 81:
		continue
	else:
		FirstPage = 'https://latesthackingnews.com/category/hackingnews/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find_all('div',attrs={"class",'entry-content clearfix'})
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			#print(i)
			data.append(LHN.spidering(i))
			time.sleep(2)
		page.clear()
with open('LHNdata_81_100.json', 'w') as f:
		json.dump(data, f)
data.clear()
'''
'''
for j in range(121):
	if j < 101:
		continue
	else:
		FirstPage = 'https://latesthackingnews.com/category/hackingnews/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find_all('div',attrs={"class",'entry-content clearfix'})
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			#print(i)
			data.append(LHN.spidering(i))
			time.sleep(2)
		page.clear()
with open('LHNdata_101_120.json', 'w') as f:
		json.dump(data, f)
data.clear()
'''

for j in range(145):
	if j < 121:
		continue
	else:
		FirstPage = 'https://latesthackingnews.com/category/hackingnews/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find_all('div',attrs={"class",'entry-content clearfix'})
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			#print(i)
			data.append(LHN.spidering(i))
			time.sleep(2)
		page.clear()
with open('LHNdata_121_144.json', 'w') as f:
		json.dump(data, f)
data.clear()
