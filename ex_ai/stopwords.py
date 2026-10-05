import nltk 
from nltk.corpus import stopwords

texto = "O seu coração é de ferro"

palavras = nltk.word_tokenize(texto)

palavras_sem_stopwords = []
palavras_stopwords = stopwords.words('portuguese')

for palavra in palavras:
    if palavra not in palavras_stopwords:
        palavras_sem_stopwords.append(palavra)

print(palavras_sem_stopwords)