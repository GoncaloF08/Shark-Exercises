media = 0
nota1 = int(input("Insira a nota 1\n"))
nota2 = int(input("Insira a nota 2\n"))
media += (nota1 + nota2)/2

if media >= 60:
    print(f"Parabens! Aluno aprovado com media de {media}")
else:
    print(f"Aluno Reprovado com media de {media}")
