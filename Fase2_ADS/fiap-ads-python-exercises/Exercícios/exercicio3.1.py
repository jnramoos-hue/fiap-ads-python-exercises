#03. Hora de decidir! Os colaboradores da sua equipe foram sorteados para ganhar um console de última geração, cada um, em razão do bom desempenho que tiveram nos últimos projetos. Por uma questão de logística, porém, a empresa pede que todos os cinco membros da equipe recebam o mesmo aparelho.
#Crie um algoritmo em que o usuário possa digitar o voto de cada um dos 5 membros da equipe e, ao final, exiba qual foi o console escolhido e com quantos votos.
#As opções são: PLAYSTATION, XBOX ou NINTENDO.

voto1 = input("Colaborador 1 informe qual priemio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO -> ")
voto2 = input("Colaborador 2 informe qual priemio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO -> ")
voto3 = input("Colaborador 3 informe qual priemio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO -> ")
voto4 = input("Colaborador 4 informe qual priemio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO -> ")
voto5 = input("Colaborador 5 informe qual priemio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO -> ")

playstation = 0
xbox = 0
nintendo = 0

if voto1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto1.upper() == "XBOX":
    xbox = xbox + 1
elif voto1.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 1 colocou um voto inexistente por isso será disconsiderado.")

if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 2 colocou um voto inexistente por isso será disconsiderado.")

if voto3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto3.upper() == "XBOX":
    xbox = xbox + 1
elif voto3.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 3 colocou um voto inexistente por isso será disconsiderado.")

if voto4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto4.upper() == "XBOX":
    xbox = xbox + 1
elif voto4.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 4 colocou um voto inexistente por isso será disconsiderado.")

if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 5 colocou um voto inexistente por isso será disconsiderado.")

if playstation > nintendo > xbox:
    print("O console escolhido foi PLaystation.")
elif nintendo > playstation > xbox:
    print("O console escolhido foi Nintendo.")
elif xbox > playstation > nintendo:
    print("O console escolhido foi XBox.")
else:
    print("Houve empate, favor entrar em contato com a direção.")