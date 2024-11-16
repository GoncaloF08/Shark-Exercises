salario = input("Qual é o nome da pasteleria?")

paoQuan = int(input("Qual é a quantidade de pães"))
paoPrec = int(input("Qual é o preço unitario do pão"))

pastQuan = int(input("Qual é a quantidade de pasteis de nata"))
pastPrec = int(input("Qual é o preço unitario do pastel de nata"))

croQuan = int(input("Qual é a quantidade de croissants"))
croPrec = int(input("Qual é o preço unitario do croissant"))

bolaQuan = int(input("Qual é a quantidade de Bolas de Berlim"))
bolaPrec = int(input("Qual é o preço unitario da Bola de Berlim"))

briQuan = int(input("Qual é a quantidade de Brigadeiros"))
briPrec = int(input("Qual é o preço unitario do Brigadeiro"))

palQuan = int(input("Qual é a quantidade de Palmiers"))
palPrec = int(input("Qual é o preço unitario do Palmier"))

print(f"\nQuantidade de pão - {paoQuan}\nValor do pão - {paoPrec}\nValor total do pão - {paoQuan*paoPrec} ")
print(f"\nQuantidade de Pasteis de Nata - {pastQuan}\nValor do Pastel de Nata - {pastPrec}\nValor total do pastel de nata - {pastQuan*pastPrec}")
print(f"\nQuantidade de Croissant - {croQuan}\nValor do Croissant - {croPrec}\nValor total do Croissant - {croQuan*croPrec} ")