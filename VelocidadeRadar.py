velocidade = int(input("Qual foi a velocidade a que o veiculo passou no radar? "))
multa = 0
if velocidade > 80:
    multa= (velocidade - 80)*2
    print(f"Estás acima do limite permitido. A multa foi gerada no valor de {multa:.2f} euros")
else:
    print("Dentro do limite. Boa Viagem!")
