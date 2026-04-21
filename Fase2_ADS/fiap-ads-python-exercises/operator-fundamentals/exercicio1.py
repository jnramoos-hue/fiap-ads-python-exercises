#solicitando os dados do aluno
email_aluno = input("Informe o e-mail do aluno: ")
nota_semestral = input("Informa a nota semestral: ")
#convertendo a nota para o formato float
nota_semestral = float(nota_semestral)
#realizando teste lógico
if nota_semestral > 8.5:
    print("ENVIANDO E-MAIL PARA {}".format(email_aluno))