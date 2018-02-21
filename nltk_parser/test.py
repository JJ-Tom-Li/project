from nltk_parser import *
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer

nltk_parser = NLTK_parser()
nltk_parser.parser(dir="news/horus scenario/",outfile="",number_of_result=50)
#nltk_parser.show_tag_of_words('NN')