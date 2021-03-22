from textblob import TextBlob
import nltk

nltk.donwload("stopwords")
from pathlib import Path
from nltk.corpus import stopwords

import pandas as pd

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

print(blob.words["juliet"])

print(blob.word_counts["romeo"])

print(blob.word_counts["thou"])

print(blob.words.count("joy"))