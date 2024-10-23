def leNota(num):
    notas=[]
    for i in range():
        dado = float(input("digite a nota:  "))
        notas.append(dado)
    return notas

def calcularMedia(notas):
    soma=0
    for i in range(len(notas)):
        soma = soma + notas[i]
    return(soma/len(notas))
n = int(input("digite o número de notas:  "))
notas = leNota(n)
print("as notas são:  ",notas)
media = calcularMedia(notas)
print(" a media é:  ", format(media,".1f"))