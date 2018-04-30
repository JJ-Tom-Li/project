from nltk_parser_modules import *
from unicodedata import normalize
from math import log
class NLTK_parser:

	def __init__(self):
		#stop words
		self.stopworddic = set(stopwords.words('english'))
		self.stopworddic.update([',','.','(',')','\'',':','\'\'','``','\'s','xa1','xa6s','xa8','r','n','b'])
		#count the frequence
		self.fdist = FreqDist()
		#count the frequency of biagrams
		self.biagram_fdist = FreqDist()
		#count the number of noun
		self.noun_count = 0
		#count the number of adj
		self.adj_count = 0
		#the tags of noun
		self.N_tag = ['NN','NNS','NNP']
	def parser(self,dir,outfile,number_of_result):
		self.__init__()
		file_number = 1		#計算分析到第幾個檔案
		for filename in os.listdir(dir):
			#If file is not end by ".txt" then continue
			if(filename[-4:]!=".txt"):
				continue
			#calculate the frequency of file 
			self.parser_freq(filename,dir)
			#count the nubmer of file
			file_number  = file_number + 1
		
		#輸出number of result個最常出現的詞
		nfdist = self.fdist.most_common(number_of_result)
		bfdist = self.biagram_fdist.most_common(number_of_result)
		if (outfile==""):
			stream = sys.stdout
			#如果沒有指定輸出檔名會直接顯示在螢幕上
			print("出現頻率前 "+str(number_of_result)+" 名：")
			self.show_freq(stream,nfdist)
			print("雙連詞出現頻率前 "+str(number_of_result)+" 名：")
			self.show_freq(stream,bfdist)
		else:
			stream = open(outfile,"w")
			for word in nfdist:
				#輸出至螢幕
				stream.write(word[0]+"\n")
			stream.write("(biagram start)\n")
			for word in bfdist:
				#輸出至螢幕
				stream.write(word[0]+"\n")
			stream.write("\n")

	def parser_freq(self,filename,dir):
		with open(dir+filename,"rb") as f:
			#讀入檔案
			SampleTXT = str(f.read())
			#去掉\r\n\r\n
			paragraphs = [p.lower() for p in SampleTXT.split('\\r\\n\\r\\n') if p]
			#斷字
			sentence=[]
			#用regular expression 斷字
			toker = RegexpTokenizer(r'\w+')
			#分段切字
			for paragraph in paragraphs:
				sentence.extend(toker.tokenize(paragraph))

			#delete stop words
			sentence = [i for i in sentence if i not in self.stopworddic ]
			
			#generate all the bigrams
			bigrams_words = nltk.bigrams(sentence)
			#calculate the conditional frequency of bigrams
			Cfdist = nltk.ConditionalFreqDist(bigrams_words)
			#tag the words
			sentence = pos_tag(sentence)
			#count
			for word in sentence:
				#if the word is a noun
				if(word[1] in self.N_tag):
					self.fdist[word[0].lower()] += 1
			#count the bigrams
			for word in self.fdist.copy():
				if(Cfdist[word]):
					#tag the maximun number of second word
					Cword = pos_tag([Cfdist[word].max()])
					#if the second word is a noun
					if(Cword[0][1] in self.N_tag):
						self.biagram_fdist[word.lower()+' '+Cfdist[word].max()]+=1	

	def show_freq(self,stream,fdist):
		for word in fdist:
			#輸出至螢幕
			stream.write("\t"+word[0]+" : "+str(word[1])+"\n")
		stream.write("\n")
				
	def show_tag_of_words(self,tag):
		word = pos_tag(self.fdist.copy())
		for show_word in word:
			if show_word[1] == tag:
				print(show_word)
	def get_text_word_token(self,text):	
		#text_word_token = []
		#for text in all_text:
			#If file is not end by ".txt" then continue
			#if(filename[-4:]!=".txt"):
			#	continue
						
			#with open(dir+filename,"r") as f:
		#讀入檔案
		SampleTXT = str(self.remove_non_ascii(text))
		#去掉\r\n\r\n
		paragraphs = [p.lower() for p in SampleTXT.split('\\r\\n\\r\\n') if p]
		#斷字
		sentence=[]
		#用regular expression 斷字
		toker = RegexpTokenizer(r'\w+')
		#分段切字
		for paragraph in paragraphs:
			sentence.extend(toker.tokenize(paragraph))
		#tag the words
		#sentence = pos_tag(sentence)
		#text_word_token.append(sentence)
		return sentence
		'''
		#count
		for word in sentence:
			#if the word is a noun
			if(word[1] in self.N_tag):
				self.fdist[word[0].lower()] += 1
				'''
		#self.find_keywords(all_text_word_token,0)
		
	def find_keywords(self,all_text_word_token,text_id,number_of_result):
		keyword = []
		tmp = []
		sentence=all_text_word_token[text_id-1]

		#tag the words
		pos_sentence = pos_tag(sentence)
		
		#count
		fdist = FreqDist()
		for word in pos_sentence:
			#if the word is a noun
			if(word[1] in self.N_tag):
				fdist[word[0].lower()]=self.tf(sentence,word[0])*self.idf(all_text_word_token,word[0])

		tmpf = fdist.most_common(number_of_result)
		for i in tmpf:
			print(i[0],":",i[1])
	def idf(self,all_text_word_token,word):
		count = 0
		for text_token in all_text_word_token:
			if word in text_token:
				count = count + 1
		return log(len(all_text_word_token)/float(count))
	def tf(self,text_token,word):
		count = 0
		for w in text_token:
			if w==word:
				count = count + 1
		return count
	#def tf_cross_idf(self,word,text_id):
	#	print()
	def remove_non_ascii(self,text):
		return normalize('NFKD', text).encode('ascii','ignore')				
						
						