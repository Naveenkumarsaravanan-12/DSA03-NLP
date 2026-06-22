from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love NLP",
    "NLP is interesting",
    "Python is powerful"
]

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(documents)

print(tfidf.toarray())
