salario = int(input("Qual é o seu salario"))
salarioR = 0
reajuste = 0
if salario< 500:
    salarioR = salario + (salario*0.15)
    reajuste = 15
elif salario < 1000:
    salarioR = salario + (salario*0.10)
    reajuste = 10
else:
    salarioR = salario + (salario * 0.05)
    reajuste = 5

print(f"O reajuste será de {reajuste}% e passará para {salarioR}")

