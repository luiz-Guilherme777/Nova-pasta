n = int (input("digite uma quanridade de números: "))
anterior=int(input())

i=1 #le numero
ordenado = True #primo é a variavel indicadora

while (i < n) and (ordenado):
    atual= int(input())
    i = i+1#leu mais um numero
    if (atual < anterior ): 
        ordenado=False
    anterior=atual
if (ordenado):
    print ("sequencia ordenada")
else:
    print(" sequencia não ordenada ordenada")