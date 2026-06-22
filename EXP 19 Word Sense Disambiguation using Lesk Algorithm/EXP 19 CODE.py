from nltk.wsd import lesk

sentence = "I went to the bank to deposit money".split()

sense = lesk(sentence, "bank")

print("Sense:", sense)
print("Meaning:", sense.definition())
