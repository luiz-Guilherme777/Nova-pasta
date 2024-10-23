def leNumeroInt():
    numero = input("digite um numero inteiro: ")
    return int(numero)#esse é só a carcaça do código para ser chamada
def soma (numero1, numero2):
    resultado = numero1 + numero2
    return resultado#esse é só a carcaça do código para ser chamada

n1 = leNumeroInt() #ele chama a função de lenumeroInt
n2 = leNumeroInt() #este chama a mesma função pela segunda vez
#res = soma(n1 , n2)#este chama a fução  soma e utiliza o n1 e n2
#print("a soma:", res)
print("a soma é :  ", soma(n1 , n2) )