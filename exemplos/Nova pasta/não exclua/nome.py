qtd =0
soma=0
mdia = 0
valor = float (input("digite um valor:  "))
while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    #entrada de valores 
    valor = float (input("digite um valor:  "))
#caso digite um valor negativo o local encerra
media = soma /qtd
print("\n total soma : ", soma)
print("\n quantidade de valores digitados:", qtd)
print("\n média dos valores:", media)