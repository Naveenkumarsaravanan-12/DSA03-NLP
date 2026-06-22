import nltk

sentence = "The black cat sits on the mat"

tokens = nltk.word_tokenize(sentence)

tags = nltk.pos_tag(tokens)

for word, tag in tags:
    if tag.startswith("NN"):
        print("Noun:", word)
