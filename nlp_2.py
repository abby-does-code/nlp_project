from textblob import TextBlob
import nltk

nltk.download("stopwords")
from pathlib import Path
from nltk.corpus import stopwords

# Error:
""" "/Users/abigailbrown/Library/Mobile Documents/com~apple~CloudDocs/Advanced_Python/NLP/nlp_2.py", line 24, in <listcomp>
    items = [item for item in items if item[0] not in stops]
NameError: name 'stops' is not defined"""

import pandas as pd

stops = stopwords.words("english")

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

"""print(blob.word_counts["juliet"])

print(blob.word_counts["romeo"])

print(blob.word_counts["thou"])

print(blob.words.count("joy"))"""

# Let's call the word counts items method
items = blob.word_counts.items()

# Use a list comprehension to eliminate any tuples containing stops
items = [item for item in items if item[0] not in stops]
print(items[:10]) #first ten items

#These are just words; no order!


## To determien teh top 20 words, let's sort the utples in items in descending order.
## We can use built-in function sorted with a key ##argument to sort tuples 
## by the element in each tuple. Tospecifcy the tuple ##element, use the "itemgetter" function from Python ##standard library


# itemgetter is a native python command
from operator import itemgetter

sorted_items = sorted(items)
print(sorted_items[:10])

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
print(sorted_items[:10])

tops = stopwords.words("english")

stops += more_stops


# Grab top 20
top20 = sorted_items[:20]

print(top20)

# Datagrame
df = pd.DataFrame(top20, columns=["word", "count"])
print(df)

import matplotlib.pyplot as plt

df.plot.bar(
    x="word", y="count", rot=0, legend=False, color=["y", "c", "m", "b", "g", "r"]
)"""
