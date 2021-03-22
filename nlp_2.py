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
print(items)