<code>class NLTK_parser</code>:

變數:

  ----<code>NLTK_parser.stopworddic</code>:儲存stopword與一些不列入統計的詞。
  
  ----<code>NLTK_parser.fdist</code>:	統計字詞出現的頻率。
  
  ----<code>NLTK_parser.biagram_fdist</code>:統計雙連詞出現的頻率。
  
  ----<code>NLTK_parser.N_tag</code>:	儲存代表名詞的pos tags，預設有NN(一般名詞)、NNS(複數名詞)與NNP(專有名詞)。

method:

  ----<code>__init__(self)</code>:Initialize variables.

  ----<code>parser(self,dir,outfile,number_of_result)</code>:讀取dir中的.txt文章,分析並排序其中出現的詞,將結果輸出至outfile中(如果outfile==""就  顯示在螢幕上).

  ----<code>parser_freq(self,filename,dir)</code>:計算filename檔案中的詞出現頻率,將結果存在NLTK_parser.fdist中.
  
  ----<code>show_freq(self,stream,fdist)</code>:讀取fdist中的字詞頻率統計，用stream輸出(file stream or stdout).
  
  ----<code>show_tag_of_words(self,tag)</code>:會把<code>self.fdist</code>中有tag屬性的名詞列出來(目前沒用到)。
  
  


