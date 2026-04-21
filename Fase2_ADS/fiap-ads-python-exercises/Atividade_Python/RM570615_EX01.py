# RM570615_EX01

# Inicializamos os contadores de vlotos para cada dia da seman com zero

votos_segunda = 0
votos_terca = 0
votos_quarta = 0
votos_quinta = 0
votos_sexta = 0

#Solicitar a quantidade de colaboradores
qtd_colaboradores = int(input("Informe quantos colaboradores irão participar da votação: "))

# Estrutura de repetição para coletar o voto de cada colaborar
for v in range(qtd_colaboradores):
    voto_valido = False

    #Usamos um while para garantir que o usuário digite um dia válido.
    #Se digitar errado, o programa pede de novo em vez de pular o voto.
    while not voto_valido:
        voto = input(f"Colaborador {v+1}, informe o dia de sua preferência (segunda, terça, quarta, quinta, sexta): ").lower()

        #Verificamos o voto com o contador correspondente
        if voto == "segunda" or voto == "segunda-feira":
            votos_segunda += 1
            voto_valido = True
        elif voto == "terca" or voto == "terca-ferira" or voto == "terça" or voto == "terça-feira":
            votos_terca += 1
            voto_valido = True
        elif voto == "quarta" or voto == "quarta-feira":
            votos_quarta += 1
            voto_valido = True
        elif voto == "quinta" or voto == "quinta-feira":
            votos_quinta += 1
            voto_valido = True
        elif voto == "sexta" or voto == "sexta-feira":
            votos_sexta += 1
            voto_valido = True
        else:
            print("Dia inválido! Por favor, digite um dia da semana de segunda a sexta.")

# Vamos descobrir qual dia da semana teve o maior nuemro de votos
maior_voto = votos_segunda
dia_vencedor = "Segunda-Feira"

if votos_terca > maior_voto:
    maior_voto = votos_terca
    dia_vencedor = "Terça-Feira"

if votos_quarta > maior_voto:
    maior_voto = votos_quarta
    dia_vencedor = "Quarta-Feira"

if votos_quinta > maior_voto:
    maior_voto = votos_quinta
    dia_vencedor = "Quinta-Feira"

if votos_sexta > maior_voto:
    maior_voto = votos_sexta
    dia_vencedor = "Sexta-Feira"

# Vamos verificar se houve empate
# Contamos quantas vezes o "maior_voto" aparece entre os dias

empates = 0

if votos_segunda == maior_voto:
    empates += 1
if votos_terca == maior_voto:
    empates += 1
if votos_quarta == maior_voto:
    empates += 1
if votos_quinta == maior_voto:
    empates += 1
if votos_sexta == maior_voto:
    empates += 1

# Modelo de saída
print("\n--- RESULTADO DA VOTAÇÃO ---")
print(f"Segunda-feira: {votos_segunda} voto(s).")
print(f"Terça-feira: {votos_terca} voto(s).")
print(f"Quarta-feira: {votos_quarta} voto(s).")
print(f"Quinta-feira: {votos_quinta} voto(s).")
print(f"Sexta-feira: {votos_sexta} voto(s).")
print("----------------------------")

# Se o maior voto apareceu mais de 1 vez, significa que há um empate
if empates > 1:
    print("RESULTADO: Houve um EMPATE entre os dias mais votados! Será necessário uma nova votação.")
else:
    print(f"RESULTADO: O dia escolhido para as lives foi {dia_vencedor} com {maior_voto} voto(s)!")


