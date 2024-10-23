n = int (input("digite um número inteiro positivo: "))

numero=2
primo = True #primo é a variavel indicadora

while (numero <= n-1) and (primo):
    if (n % numero == 0 ): #se não é diaponivel por número
        primo=False
    numero=numero + 1
if (primo):
    print ("é primo")
else:
    print(" não é primo")