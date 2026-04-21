# RM570615_EX02

# Recebemos o valor do carro
valor_carro = float(input("Digite o valor do carro: "))

# Calculamos o preço à vista com (20% de desconto)
# Esse valor será a base para todos os outros cálculos da tabela
preco_a_vista = valor_carro * 0.80

# Exibimos a primeira parte do modelo de saída
print(f"Preço final à vista com desconto de 20%: R$ {preco_a_vista:.2f}")

# Loop para com range para as parcelas (6 até 60, pulando de 6 em 6)
# Juros começa em 3% para 6 parcelas e tem um range de 3 em 3
perc_juros = 3

for parcelas in range(6, 61, 6):
    #O acréscimo é calculado sobre o preço à vista
    valor_acrescimo = preco_a_vista * (perc_juros / 100)
    preco_final = preco_a_vista - valor_acrescimo

    #calculando o valor de cada parcela
    valor_parcela = preco_final / parcelas

    # Exibimos os dados formatados
    # Usamos o \t para criar o espaçamento de tabela
    print(f"R$ {preco_final:.2f} \t {parcelas} \t {valor_parcela:.2f}")

    #Acrécimo de juros em 3% para a proxima linha da tabela
    perc_juros += 3


