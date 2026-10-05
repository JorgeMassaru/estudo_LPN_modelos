import nltk
from nltk import ngrams

texto = "O seu coração é de ferro"

palavras = nltk.word_tokenize(texto)

n = 2

bigrams = list(ngrams(palavras, 2))

print(bigrams)
