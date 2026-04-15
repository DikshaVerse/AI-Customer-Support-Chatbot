import nltk
import string
from nltk.tokenize import word_tokenize

# nltk.download('punkt_tab')


def preprocess(text):
   text=text.lower()
   text=text.translate(str.maketrans('','',string.punctuation))
   tokens=word_tokenize(text)
   return tokens


print(preprocess("Where is my order??"))



