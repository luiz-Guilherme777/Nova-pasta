class Contato: 
    def __init__(self, nome, endereco, email): 
        self.nome = nome 
        self.endereco = endereco 
        self.email = email 
class Agenda: 
    def __init__(self): 
        self.contatos = []
    def adicionar_contato(self, contato): 
        self.contatos.append(contato) 
    def remover_contato(self, contato): 
        self.contatos.remove(contato)
    def listar_contatos(self): 
        for contato in self.contatos: 
            print("Nome:", contato.nome)
            print("Endereço:", contato.endereco) 
            print("E-mail:", contato.email) 
agenda = Agenda() 
contato1 = Contato("João", "Rua A, 123", "joao@example.com") 
contato2 = Contato("Maria", "Rua B, 456", "maria@example.com") 
agenda.adicionar_contato(contato1) 
agenda.adicionar_contato(contato2) 
agenda.listar_contatos() 
agenda.remover_contato(contato1) 
agenda.listar_contatos()
#Ele inicializa os atributos do contato: nome, endereco e email.
#__init__: O método construtor da classe Agenda inicializa uma lista vazia chamada contatos, que será usada para armazenar objetos Contato.
#adicionar_contato: Este método adiciona um objeto Contato à lista contatos.
#remover_contato: Este método remove um objeto Contato da lista contatos
#listar_contatos: Este método imprime os detalhes de cada contato na lista contatos. Para cada contato, ele imprime o nome, endereco e email.
#Criação da Agenda e Contatos:
#-Cria uma instância da classe Agenda chamada agenda.
#-Cria dois objetos Contato chamados contato1 e contato2, com informações específicas (nome, endereço, e-mail).
#Adição dos Contatos:
#-Adiciona contato1 e contato2 à lista de contatos da agenda usando o método adicionar_contato.
#Listagem dos Contatos:
#Imprime os detalhes dos contatos na agenda. Neste ponto, a lista contém contato1 e contato2.
#Remoção do Contato:
#-Remove contato1 da lista de contatos da agenda usando o método remover_contato.
#Listagem dos Contatos Após Remoção:
#-Imprime novamente os detalhes dos contatos na agenda. Agora, a lista contém apenas contato2, pois contato1 foi removido.