import nltk 

texto1 = "O seu coração é de ferro"
texto2 = "O seu coração é de aço"

tokens1 = []
Tokens2 = []

tokens1 = nltk.word_tokenize(texto1)
tokens2 = nltk.word_tokenize(texto2)

interseccao = 0 
for p1 in tokens1:
    for p2 in tokens2:
        if(p1 == p2):
            interseccao = interseccao + 1

uniao = 0
tam_texto1 = len(texto1)
tam_texto2 = len(texto2)
uniao = (tam_texto1 + tam_texto2) - interseccao

jaccard = (interseccao/uniao) * 100

print (jaccard)