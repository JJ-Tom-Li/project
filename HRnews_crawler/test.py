'''
A = '1832457903485'
A += '123'
print('字串')
print(A)
print('迴圈')
b = []
for i in range(10):
	if i == 1:
		continue
	elif i > 8:
		break
	print(i)
print('陣列')
c = []
c.append('1')
c.append('43576')
for item in c:
	print(item)
'''
FirstPage = 'https://www.hackread.com/sec/'
for j in range(11):
	if j == 0:
		continue
	elif j == 1:
		print(FirstPage)
	else:
		FirstPage = 'https://www.hackread.com/sec/'
		FirstPage = FirstPage + 'page/' + str(j) + '/'
		print(FirstPage)