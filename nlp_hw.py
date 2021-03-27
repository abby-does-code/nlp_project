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


blob = TextBlob(Path("book_of_john_text.txt").read_text())

# Mmkay.... we're trying to grab words

items = blob.word_counts.items()
items = [item for item in items if item[0] not in stops]
# print(items[:10])  # Another checkpoint

## Functional at this ^^^ point!

from operator import itemgetter

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
# print(sorted_items[:10])

##Functional at this ^^^ point!


stops = stopwords.words("english")
more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall"]
stops += more_stops

# Grab the top 15:
top15 = sorted_items[:15]
print(top15)


# Time for wordcloud....

import wordcloud

"""
mask_image = imageio.imread("mask_heart.png")
wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")"""

wordcloud = wordcloud.generate(blob)
wordcloud = wordcloud.to_file("BookOfJohn.png")

plt.imshow(wordcloud)
print("done")

#AttributeError: module 'wordcloud' has no attribute 'generate'
