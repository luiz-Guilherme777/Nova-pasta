from datetime import datetime
import pytz


class ContaCorrente():

#faz a data e hora ficar organizado
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H: %M: %S:')

    def __init__(self, nome, cpf , agencia , num_conta):
        self.nome = nome
        self.cpf = cpf 
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    #quando chamado ele mostra o saldo dentro de conta
    def consultar_saldo(self):
        print('seu saldo atual é de R${:,.2f}'.format(self.saldo))
        pass

    #dposita e soma o diheiro
    def depositar_dinheiro(self , valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        pass

    #põe um limite de saque que ele não permite passar de -1000
    def limite_conta(self):
        self.limite = -1000
        return self.limite

    #serve para sacar o money
    def sacar_dinheiro(self , valor):
        if self.saldo -valor < self.limite_conta():
            print("saldo insuficiente digite um valor menor")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((valor , self.saldo, ContaCorrente._data_hora()))
        pass

    #mostra o historico de transações
    def consultar_historico_transacoes(self):
        print("histórico de transacoes:  ")
        for transacao in self.transacoes:
            print (transacao)

    #transfere o valor de uma conta para outra
    def transferir(self, valor, conta_destino):
        self.saldo -=valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))

        
#programa

conta_lira = ContaCorrente("lira", "111.222.333-45", "1525", "1234")
conta_lira.consultar_saldo()

#depositar dinheiro
conta_lira.depositar_dinheiro(10000)
conta_lira.consultar_saldo()

#sacar
conta_lira.sacar_dinheiro(1000000)
conta_lira.consultar_saldo() 

#consulta o historico de tranzações feitas
conta_lira.consultar_historico_transacoes()