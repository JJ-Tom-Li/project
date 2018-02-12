from nltk_parser_modules import *
class NLTK_parser:
	#stop words
	stopworddic = set(stopwords.words('english'))
	#count the frequence
	fdist = FreqDist()
	def __init__(self):
		self.stopworddic.update([',','.','(',')','\'',':','The','\'\'','``','\'s'])
		self.fdist = FreqDist()
		
	def parser(self,dir,outfile,number_of_result):
		sentence = []		#存切出來的詞
		file_number = 1		#計算分析到第幾個檔案
		for filename in os.listdir(dir):
			#If file is not end by ".txt" then continue
			if(filename[-4:]!=".txt"):
				continue
			#calculate the frequency of file 
			self.parser_freq(filename,dir)
			#count the nubmer of file
			file_number  = file_number + 1
		#排序
		nfdist=sorted(self.fdist, key=self.fdist.get, reverse=True)
		
		if(outfile==""):
			#如果沒有指定輸出檔名 直接顯示在螢幕上
			print("出現頻率前 "+str(number_of_result)+" 名：")
			for word,index in zip(nfdist,range(0,number_of_result)):
				if(index==20):
					#如果顯示二十個就結束
					break
				#輸出至螢幕
				print("\t"+word+" : "+str(self.fdist[word]))
		else:		
			with open(outfile,"w") as outf:	
				outf.write("出現頻率前 "+str(number_of_result)+" 名：\n")
				for word,index in zip(nfdist,range(0,number_of_result)):
					if(index==20):
						#如果顯示二十個就結束
						break
					#輸出至檔暗
					outf.write("\t"+word+" : "+str(self.fdist[word])+"\n")
				
	def parser_freq(self,filename,dir):
		with open(dir+filename,"rb") as f:
					#讀入檔案
					SampleTXT = str(f.read())
					#去掉\r\n\r\n
					paragraphs = [p for p in SampleTXT.split('\\r\\n\\r\\n') if p]
					#斷字
					sentence=[]
					for paragraph in paragraphs:
						sentence.extend(word_tokenize(paragraph))

					#delete stop words
					sentence = [i for i in sentence if i not in self.stopworddic ]

					#統計頻率
					for word in sentence:
						self.fdist[word.lower()] += 1
