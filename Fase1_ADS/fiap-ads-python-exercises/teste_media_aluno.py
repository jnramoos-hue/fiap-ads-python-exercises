nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
print(f"A média do aluno é: {media}")
if media >= 6:
    print("O aluno foi aprovado!!!")
else:
    print("O aluno foi reprovado!!!")