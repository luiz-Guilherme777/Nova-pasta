class ContaCorrente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf 
        self.saldo = 0
        

conta_lira = ContaCorrente("lira","111.222.333-45")

print('saldo da conta é' , conta_lira.saldo)
print(conta_lira.cpf)