#Variável para armazenar o peso total das caixas
peso_total = 0.0
#loop para repetir por 100 vezes a solicitação do peso da caixa
for x in range(1, 101):
    #Para cada volta do loop solicitar o peso da caixa
    peso_atual = float(input("Informe o peso da caixa: "))
    #para cada peso solicitado, somar ao peso total
    peso_total = peso_total + peso_atual

#Ao final do loop, calcular a media aritmética
media = peso_total / 100

#exibição dos resultados
print(f"O peso total de caixas é de: {peso_total:.2f}.\nA média de peso é de: {media:.2f}. ")
