def leMatriz(dimensao):
    mat = [[] for i in range(dimensao)]
    for i in range(dimensao):
        for j in range(dimensao):
            num = int(input("("+str(i+1)+","+str(j+1)+"): "))
            mat[i].append(num)
    return mat
def imprimeMatriz(mat):
    for linha in mat:
        for numero in linha:
           print(numero, end=" ")
#imprime números na mesma linha separados por espaço
        print() #apos impressão de uma linha, pula uma linha
dimensao = int(input("Digite a dimensão da matriz: "))
mat = leMatriz(dimensao)
imprimeMatriz(mat)