# Uma universidade realizará uma competição acadêmica. Para esta competição, só serão aceitos estudantes que sejam maiores de idade.

#Crie um programa que receba o RM e a idade de um aluno, e exiba uma mensagem confirmando o cadastro apenas caso o estudante seja maior.

rm = input("Por favor, insira o seu RM: ")
idade = int(input("Por favor, insira a sua idade: "))
if idade >= 18:
    print(f"Seu cadastro foi realizado com sucesso, aluno de RM {rm}")
    print("Os detalhes serão enviados para o seu e-mail!")
else:
    autorizacao = input("Você tem autorização dos seus pais? S- SIM, N- NÃO : ")
    if autorizacao == "S":
        print(f"Sua participação foi autorizada com sucesso, aluno de RM {rm}")
        print("Mais informações serão enviadas para o email dos responsáveis.")
    else:
        print("Sua participação foi negada, pois você não é maior de idade.")

print("O programa será finalizado!")