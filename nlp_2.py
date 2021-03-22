from textblob import TextBlob
import nltk

# nltk.download("stopwords")
from pathlib import Path
from nltk.corpus import stopwords

import pandas as pd

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

print(blob.words["juliet"])

print(blob.word_counts["romeo"])

print(blob.word_counts["thou"])

print(blob.words.count("joy"))

# Let's call the word counts items method
items = blob.word_counts.items()
print(items)

items = [item for item in items if item[0] not in stops]
print(items[:10])

# itemgetter is a native python command
from operator import itemgetter

sorted_items = sorted(items)
print(sorted_items[:10])

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
print(sorted_items[:10])


stops = stopwords("english")

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
)
