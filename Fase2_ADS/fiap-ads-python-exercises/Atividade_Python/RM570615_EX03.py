# RM570615_EX03.py

divida =float(input("Informe o valor da dívida: "))

# Cabeçalho direto
print("\nDivida \t\t Juros \t\t Parcelas \t Valor Parcela")

# Caso de 1 parcela
print(f"R$ {divida:.2f} \t R$ 0.00 \t 1 \t\t R$ {divida:.2f} \t R$ {divida:.2f}")

# Loop para as parcelas 3, 6, 9, 12.
perc_juros = 10

for qtd_parcelas in range(3, 13, 3):
    valor_juros = divida * (perc_juros / 100)
    valor_total = divida + valor_juros
    valor_parcela = valor_total / qtd_parcelas

    # Saída formatada com apenas um ou dois \t para alinhamento básico
    print(f"R$ {valor_total:.2f} \t R$ {valor_juros:.2f} \t {qtd_parcelas} \t\t R$ {valor_parcela:.2f}")

    # Aumenta o juros em 5% para a próxima linha
    perc_juros += 5
