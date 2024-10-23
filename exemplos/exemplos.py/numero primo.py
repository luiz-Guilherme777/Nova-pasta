n = int (input("digite uma quanridade de números: "))
numero= 2
divisores = 0#dividores é a variavel contadora

while (numero <= n-1):
    if (n % numero == 0 ): #se não é diaponivel por número
        divisores = divisores + 1
    numero=numero+1

if(divisores == 0):
    print("é primo")
elif(divisores ==10):
    print("não é primo.possui um divisor diferente de 1 e ",n)
else:
    print("não é primo.possui",divisores,"divisores diferentes de 1 e",n)   