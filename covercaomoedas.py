escolha = int(input("Moedas a converter\n1- Dolar\n2- Real\n3- Bat\n4- Iene\n5- Libra\nQue moeda quer converter?\n"))
euro = int(input("Quantos euros quer converter?\n"))
if escolha == 1:
    print(f"Euro - {euro}\nDolar - {euro * 1.0583}")
if escolha == 2:
    print(f"Euro - {euro}\nReal - {euro * 6.1335}")
if escolha == 3:
    print(f"Euro - {euro}\nBat - {euro*31.20}")
if escolha == 4:
    print(f"Euro - {euro}\nIene - {euro*164.36}")
if escolha == 5:
    print(f"Euro - {euro}\nLibra - {euro*0.83455}")


