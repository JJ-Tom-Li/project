import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from PageStart import PageStart
import json
import codecs
import time

hr = PageStart()

'''
res = requests.get('https://www.hackread.com/sec/', headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
soup = BeautifulSoup(res.text, "lxml")

link = soup.find_all('a',attrs={"class",'link'})
page = []
for p in link:
	page.append(p.get('href'))
data = []
for i in page:
	
	#print(hr.spidering(i))

	data.append(hr.spidering(i))


#print(data)

with open('HRdata.json', 'w') as f:
		json.dump(data, f)
		#f.write(json_text)
'''

FirstPage = 'https://www.hackread.com/sec/'
data = []
page = []
'''
for j in range(11):
	if j == 0:
		continue
	elif j == 1:
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_1_10.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(21):
	if j < 11:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_11_20.json', 'w') as f:
		json.dump(data, f)
data.clear()
'''
'''
for j in range(31):
	if j < 21:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_21_30.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(41):
	if j < 31:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_31_40.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(51):
	if j < 41:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_41_50.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(61):
	if j < 51:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_51_60.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(71):
	if j < 61:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_61_70.json', 'w') as f:
		json.dump(data, f)
data.clear()
'''

'''
for j in range(81):
	if j < 71:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_71_80.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(101):
	if j < 81:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_81_100.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(121):
	if j < 101:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_101_120.json', 'w') as f:
		json.dump(data, f)
data.clear()

'''
for j in range(141):
	if j < 121:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_121_140.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(161):
	if j < 141:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_141_160.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(181):
	if j < 161:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_161_180.json', 'w') as f:
		json.dump(data, f)
data.clear()

for j in range(186):
	if j < 181:
		continue
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		res = requests.get(FirstPage, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'})
		soup = BeautifulSoup(res.text, "lxml")
		link = soup.find('div',attrs={"class",'article-box'}).find_all('h2')
		for p in link:
			page.append(p.find('a')['href'])
		for i in page:
			data.append(hr.spidering(i))
			time.sleep(3)
		page.clear()
with open('HRdata_181_185.json', 'w') as f:
		json.dump(data, f)
data.clear()
