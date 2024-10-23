fruta = input("Digite o nome de uma fruta: ")
print("A fruta digitada foi: " + fruta)

#------------------------------------------------------------

codigo = int(input("Digite o código do funcionário "))
nome = input("Digite o nome do funcionário ")
salario = float(input("Informe o salário do funcionário "))
ativo = True

print ("Código: %d "% codigo)
print ("Nome : %s "% nome)
print ("Salário: %.2f "% salario)
print ("Ativo: %r "% ativo)

#--------------------------------------------------------------

A = 5 
B = 15
C = 20

print ("A == B AND B > C : ", A == B and B > C)
print ("A < B OR B > C : ", A < B or B > C)
print ("not A == B : ", not A == B)

#A == B AND B > C : False
#A < B OR B > C : True
#not A == B : True
