notas = []
n = int(input("digite a quantidade de notas: "))
for i in range(n):
    dado = float(input("digite a nota: "))
    notas.append(dado)
print(notas)

soma = 0
for i in range(len(notas)):
    soma=soma+notas[i]
media = soma/n
print(format(media,".1f"))