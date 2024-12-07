tipoTransporte = int(input("Qual é o tipo de transporte:\n1- Carro\n2- Barco\n3- Avião\n4- Comboio\n"))
Kilometro = int(input("A viagem é de quantos kilometros? "))
pessoasQuan = int(input("Quantas pessoas vão na viagem? "))
precototal = 0
precokm = 0

match tipoTransporte:
    case 1:
        precokm = 10
    case 2:
        precokm = 7
    case 3:
        precokm = 5
    case 4:
        precokm = 13

precototal = precokm*Kilometro*pessoasQuan
print(f"O preço total da viagem de {Kilometro} kilometros e com {pessoasQuan} pessoas será de {precototal}")


