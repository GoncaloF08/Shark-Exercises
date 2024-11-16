altura = int(input("Insira a altura"))
comprimento = int(input("Insira o comprimento"))

latas = 0

area = altura*comprimento

tinta = (2*area)
tintaL = tinta
while tintaL >=10:
    latas += 1
    tintaL -= 10

if tintaL != 0:
    latas+=1
    tintaL=0

print(f"A parede tem {area} metros quadrados e é preciso {tinta} litros de tinta para a pintar, logo {latas} latas.")


