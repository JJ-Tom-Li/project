class NLTK_parser:
<code>NLTK_parser.fdist</code>:	統計字詞出現的頻率
---- NLTK_parser.stopworddic:
	儲存stopword與一些不列入統計的詞
---- __init__(self):
	Initialize variables.
---- parser(self,dir,outfile,number_of_result):
	讀取dir中的.txt文章,分析並排序其中出現的詞,將結果輸出至outfile中(如果outfile==""就顯示在螢幕上).
---- parser_freq(self,filename,dir):
	計算filename檔案中的詞出現頻率,將結果存在NLTK_parser.fdist中.
	
