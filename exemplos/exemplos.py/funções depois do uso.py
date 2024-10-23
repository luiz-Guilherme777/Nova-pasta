def main():
    n1 = leNumeroInt()
    n2 = leNumeroInt()
    res = soma(n1, n2)
    print("a soma é:  ", res)

def leNumeroInt():
    numero = input("digite um numero inteiro:")
    return int(numero)
def soma(numero1 , numero2):
    resultado = numero1 + numero2
    return resultado
main()