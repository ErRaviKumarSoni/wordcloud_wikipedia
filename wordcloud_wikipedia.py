import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image
import numpy as np

currdir = os.path.dirname(__file__)
def get_wiki(query):
    title = wikipedia.search(query)[0]
    page= wikipedia.page('title')
    return page.content

def creat_wordcloud(text):
    Mask = np.array(Image.open(os.path.join(currdir,"Name.png")))
    stopwords = set (STOPWORDS)
wc = WordCloud(background_Color="black",
                   mask = mask,
                   max_words=200,stopwords=stopwords)
wc.generate(text)

wc.to_file(os.path.join(currdie,"wc.png")

create_wordcloud(get_wiki("python programming language"))

  
    
    
    