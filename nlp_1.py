# Through machine learning, trying to teach computers
##how we communicate and process information

from textblob import TextBlob


text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

print(blob)

# print(blob.sentences)  # Prints the separate sentences

# print(blob.words)  # Prints the separate words

# print(blob.tags)  # Nouns, pronouns, verbs, etc.

# print(blob.noun_phrases)

print(blob.sentiment)  # Module has been trained on movie reviews
# Closer to 1 = more subjective
# Closer to 0 = more neutral (polarity)

print(round(blob.sentiment.polarity, 3))

print(round(blob.sentiment.subjectivity, 3))

sentences = blob.sentences
for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)
    print(round(sentence.sentiment.polarity, 3))

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)

blob.detect_language()

spanish = blob.translate(to="es")

print(spanish)


from textblob import Word

index = Word("index")
print(index.pluralize())

cacti = Word("cacti")
print(cacti.singularize())

word = Word("theyr")
print(word.spellcheck())
corrected_word = word.correct()

sentence = TextBlob("Ths sentense has mispelled wrds.")
corrected_sentence = sentence.correct()


# print(corrected_sentence)
# print(corrected_word)

##########################################################
##########################################################

# Stemming algorithms work by cutting off the end or beginning of #the word; reduces diffeerent morphoological variants of a word #to the root base.

##Varieties = variety
##Studies = study

from textblob import Word

word1 = Word("studies")
word2 = Word("varieties")

print(word1.lemmatize())
print(word2.lemmatize())


########################
happy = Word("happy")

print(happy.definitions)

# Method synsets

for synset in happy.synsets:
    print(synset)

# To access object in synsets, we use the lemmas object
for synset in happy.synsets:
    for lemma in synset.lemmas():
        print(lemma)
        print(lemma.name())
lemmas = happy.synsets[0].lemmas()
print(lemmas)

for lemma in lemmas[0].antonyms():
    print(lemma.name())


##############################################################
# Looking for stop words i think
# Stop words are common words unnecessray for analysis

import nltk


nltk.download("stopwords")

from nltk.corpus import stopwords

stops = stopwords.words("English")
print(stops)

blob = TextBlob("Today is a beautiful day.")
print(blob.words)

cleaned_list = [word for word in blob.words if word not in stops]
print(cleaned_list)


#Note: ran this code after the craziness on 3/24; functional
