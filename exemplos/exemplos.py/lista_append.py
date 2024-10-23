notas = []
n = int(input("entre com o numero de notas:  "))
for i in range(n):
    dado = float(input("entre com a nota" + str(i+1)+ ":"))
    notas.append(dado)
print(notas)