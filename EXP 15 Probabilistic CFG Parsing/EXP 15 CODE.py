import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'John' [1.0]
VP -> 'runs' [1.0]
""")

parser = ViterbiParser(grammar)

sentence = "John runs".split()

for tree in parser.parse(sentence):
    print(tree)
