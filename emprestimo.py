valorImovel = int(input("Qual é o valor do imóvel"))
salarioCliente = int(input("Qual é o seu salario"))
mesesPagamento = int(input("Em quantos anos quer pagar o imovel?"))
mesesPagamento*=12
prestacao = valorImovel/mesesPagamento
print(f"A prestação é {prestacao}, e 30% do seu salario é {salarioCliente * 0.30}")

if (salarioCliente*0.30) <= prestacao:
    print("Não foi possivel fazer o emprestimo")
else:
    print("O emprestimo foi aceite")