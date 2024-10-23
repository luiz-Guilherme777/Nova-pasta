class tv:
    def __init__(self, cor, tamanho):
        self.cor = cor
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "netflix"
        self.volume = 10

    def mudar_canal(self,novo_canal):
        self.canal = novo_canal

#programa
tv_sala = tv(cor='preta', tamanho=55)
tv_quarto = tv('branca',29)

tv_sala.mudar_canal('globo rural')
tv_quarto.mudar_canal('youtube')


print(tv_sala.canal)#imprime "netflix"
print(tv_quarto.canal)#imprime "netflix"
print(tv_sala.cor)
print(tv_sala.tamanho)
print(tv_sala.volume)
print(tv_quarto.tamanho)