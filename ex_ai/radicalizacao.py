import nltk 

texto = "Olá, como você está?"

palavras = nltk.word_tokenize(texto)

radicalizador = nltk.SnowBallStemmer(palavras)

radical = []

for palavra in palavras:
    radicais = radicalizador.stem(palavra)
    radical.append(radicais)

print(radical)