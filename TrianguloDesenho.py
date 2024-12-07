numLinhas = (int(input("Quantas linhas quer no triangulo?")))
count = 0

linha = 1
ponto = ""
for count in range ((numLinhas*2)+1):
    if count > numLinhas:
        for i in range(linha):
            ponto= ponto[:-1]
    else:
        for i in range (linha):
            ponto += "*"
    print(ponto)





