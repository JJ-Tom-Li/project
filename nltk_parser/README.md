<code>class NLTK_parser</code>:

變數:

  ----<code>NLTK_parser.fdist</code>:	統計字詞出現的頻率

  ----<code>NLTK_parser.stopworddic</code>:儲存stopword與一些不列入統計的詞

method:

  ----<code>__init__(self)</code>:Initialize variables.

  ----<code>parser(self,dir,outfile,number_of_result)</code>:讀取dir中的.txt文章,分析並排序其中出現的詞,將結果輸出至outfile中(如果outfile==""就  顯示在螢幕上).

  ----<code>parser_freq(self,filename,dir)</code>:計算filename檔案中的詞出現頻率,將結果存在NLTK_parser.fdist中.


