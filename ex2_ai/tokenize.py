import nltk
import ngrams
from nltk.corpus import stopwords

corpus = ["a flor e a nausea brincam", "a flor não brinca com a nausea dos outros", "Odeio catar flores quando estou com nausea"]
corpus_min = [text.lower() for text in corpus]

tokens = []

for text in corpus_min:
    text_tokenizado = nltk.word_tokenize(text)
    tokens.append(text_tokenizado) 

palavra_sem_stopword = []
palavra_stopwords = stopwords.word('english')

for token in tokens:
    guardar = []
    for palavra in token:
        if palavra not in palavra_stopwords:
            guardar.append(palavra)
    palavra_sem_stopword.append(guardar)

lematizador = nltk.stem.WordNetLemmatizer()
lemas = []

for palavras in palavra_sem_stopword:
    guardar = []

    for i in palavras:
        lematize = lematizador.lemmatize(i)
        guardar.append(lematize)
    lemas.append(guardar)

for text in lemas:
    n = 1 
    unigram = list(ngrams(lemas, n))

for text in lemas:
    n = 2 
    bigram = list(ngrams(lemas, n))

for text in lemas:
    n = 3 
    trigrams = list(ngrams(lemas, n))
