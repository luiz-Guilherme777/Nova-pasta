class tv:
    def __init__(self):
        self.cor = "preta"
        self.ligada = False
        self.tamanho = 55
        self.canal = "netflix"
        self.volume = 10

#programa
tv_sala = tv()
tv_quarto = tv()

print(tv_quarto.canal)#imprime "netflix"
print(tv_quarto.canal)#imprime "netflix"
print(tv_sala.cor)
print(tv_sala.tamanho)
print(tv_sala.volume)

