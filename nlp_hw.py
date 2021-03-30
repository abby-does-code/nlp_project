# START#

""" Use this text file  - book of John text.txt  downloadto create a wordcloud of the top 15 words that are the most recurring. Make sure to remove all stop words. Use only noun words for this analysis.To get a good idea of what the book of John is about, it would be better to eliminate additional stop words that are found in the context of the Bible. Please eliminate these additional words from your WordCloud:

thy, ye, verily, thee, hath, say, thou, art, shall"""

from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

from pathlib import Path
import pandas as pd


stops = stopwords.words("English")
## print(stops)  # Let's use this as a checkpoint

# Functional at this ^^^ point

more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall"]
stops += more_stops

blob = TextBlob(Path("book_of_john_text.txt").read_text())

# Mmkay.... we're trying to grab words

items = blob.word_counts.items()
items = [item for item in items if item[0] not in stops]
# print(items[:10])  # Another checkpoint

## Functional at this ^^^ point!

# get JUST the nouns

nouns = blob.noun_phrases

noun_list = [item for item in items if item[0] in nouns]
print(items[:10])


from operator import itemgetter

sorted_nouns = sorted(noun_list, key=itemgetter(1), reverse=True)
# print(sorted_items[:10])

##Functional at this ^^^ point!


# Grab the top 15:
top15 = sorted_nouns[:15]
print(top15)


# Time for wordcloud....

from wordcloud import WordCloud


wordcloud = WordCloud(colormap="prism", background_color="white")

wordcloud = wordcloud.generate(str(top15))
wordcloud = wordcloud.to_file("BookOfJohn.png")

# matplotlib
import matplotlib.pyplot as plt


# Maybe show me?
plt.imshow(wordcloud)
print("done")
