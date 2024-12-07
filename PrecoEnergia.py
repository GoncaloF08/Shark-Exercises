kWh = int(input("Qual foi a quantidade de kWh consumidos?"))
instalacao = input("Qual é o tipo de instalação?\nR- Residencial\nC- Comercial\nI- Industrial\n")
preco = 0.0

match instalacao.upper():
    case "R":
        if kWh <= 500:
            preco = 0.40
        else:
            preco = 0.65
    case "C":
        if kWh <= 1000:
            preco = 0.55
        else:
            preco = 0.60
    case "I":
        if kWh <= 5000:
            preco = 0.55
        else:
            preco = 0.60
    case _:
        print("Opção invalida")
if preco != 0:
    print(f"O preço vai ser {preco}")
