def posOuNeg(numero):
    if numero<0:
        return 'N'
    elif numero > 0:
        return'P'
    else:
        return'z'
numero = int(input("digite um numero:  "))
resultado = posOuNeg(numero)
print(f"resultado é:  {resultado}")