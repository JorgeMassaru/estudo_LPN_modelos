import nltk

texto = "O seu coração é de ferro"

palavras = nltk.word_tokenize(texto)

lematizador = nltk.stem.WordNetLemmatizer() 

Lemas = []

for palavra in palavras:
    lematize = lematizador.lemmatize(palavra)
    Lemas.append(lematize)

print(Lemas)