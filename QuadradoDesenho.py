lado = int(input("Qual é o lado?"))
ponto = "";

for i in range (lado):
    for a in range (lado):
        ponto+="*"
    print(ponto)
    ponto = ""