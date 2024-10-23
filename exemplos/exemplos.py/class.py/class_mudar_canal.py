class tv:
    def __init__(self):
        self.cor = "preta"
        self.ligada = False
        self.tamanho = 55
        self.canal = "netflix"
        self.volume = 10

    def mudar_canal(self,novo_canal):
        self.canal = novo_canal

#programa
tv_sala = tv()
tv_quarto = tv()

tv_sala.mudar_canal('globo rural')
tv_quarto.mudar_canal('youtube')


print(tv_sala.canal)#imprime "netflix"
print(tv_quarto.canal)#imprime "netflix"
print(tv_sala.cor)
print(tv_sala.tamanho)
print(tv_sala.volume)

