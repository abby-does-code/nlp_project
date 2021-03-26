import spacy

# Note: shortcut doesn't work
# nlp = spacy.load('en')

# Long way:
nlp = spacy.load("en_core_web_sm")

document = nlp(
    "In 1994, Time Berners-Lee founded the World Wide WEb Consortium (W3C), devoted to"
    + "developing web technologies"
)

for entity in document.ents:
    print(entity.text, ":", entity.label_)

"""ERROR: OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a Python package or a valid path to a data directory."""

from pathlib import Path
