notaA = float(input("informe a primeira nota: "))
notaB = float(input("infoerme a segunda nota: "))
#calcular media
mediafinal = (notaA + notaB) / 2
#verificação
if mediafinal >+ 7.0:
    print("a media : %.1f - aprovado" % mediafinal)
else:
    print("a media : %.1f - reprovado" % mediafinal)