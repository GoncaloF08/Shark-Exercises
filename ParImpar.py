num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))
num3 = num1

if num1 > num2:
    num1 = num2
    num2 = num3

escolha = int(input(f"Quer saber os numeros pares ou impares entre {num1} e {num2}?\n1- pares\n2- impares"))

for num3 in range (num1, num2):
    if (escolha == 1 and num3 % 2 == 0) or (escolha == 2 and num3 % 2 == 1):
        print(num3)









