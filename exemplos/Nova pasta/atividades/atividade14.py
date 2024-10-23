numeros = []
for i in range(10):
    try:
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida!!!")
soma = sum(numeros)
media = soma / len(numeros)
print("Soma:", soma)
print("Média:", media)
#inicia com a criação da lissta números vazia, pronta para receber um numero digitado pelo usuario
# depois inicia um loop de 0 a 9  que ira receber 10 numeros
#try executa o código dentro do bloco, depois solicita o usuario a digitar uma numero
#int(...): Tenta converter a entrada do usuário para um número inteiro.
#numeros.append(numero): Adiciona o número convertido à lista numeros.
#except ValueError:: Captura exceções do tipo ValueError que ocorrem se a conversão para inteiro falhar (por exemplo, se o usuário digitar texto não numérico).
#print("Entrada inválida!!!"): Exibe uma mensagem de erro para informar ao usuário que a entrada não é válida.
#soma = sum(numeros): Calcula a soma de todos os números na lista numeros.
#media = soma / len(numeros): Calcula a média dos números. len(numeros) fornece o número total de elementos na lista.
#print("Soma:", soma): Exibe a soma dos números.
#print("Média:", media): Exibe a média dos números.