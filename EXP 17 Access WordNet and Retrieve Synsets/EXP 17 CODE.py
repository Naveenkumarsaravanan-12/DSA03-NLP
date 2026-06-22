import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet

word = "bank"

for synset in wordnet.synsets(word)[:3]:
    print(synset.name())
    print("Meaning:", synset.definition())
