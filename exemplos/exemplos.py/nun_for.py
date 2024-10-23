n = int(input("Digite um número: "))
anterior = int(input())

ordenado = True # ordenado é a variavel indicadora

for i in range (n-1):
    atual = int(input())
    if atual < anterior :
        ordenado = False
        break
    anterior = atual

if ordenado :
    print("Sequência Ordenada")
else: 
    print("Sequência Não Ordenada")