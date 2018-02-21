import nltk
import re
import tkinter
import os
import sys
from nltk.tokenize import word_tokenize,sent_tokenize,RegexpTokenizer
from nltk.chunk import ne_chunk
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.tree import Tree
from nltk.probability import FreqDist
from nltk.probability import ConditionalFreqDist
from nltk.text import Text