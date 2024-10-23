texto=input("digite um texto")
pontuacao=[".",",",":",";","!","?"]
#remove os sinais de pontuação
for p in pontuacao:
    texto = texto.replace(p,"")
#split devolve lista