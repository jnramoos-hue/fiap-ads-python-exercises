# RM570615_EX04.py



# Validação do tipo de investimento
tipo = int(input("""
Escolha o tipo do investimento
 1.CDB 
 2.LCI 
 3.LCA 
 Digite o tipo do investimento (1,2 ou 3): """))

while tipo < 1 or tipo > 3:
    print("\n----Tipo inválido!----")
    tipo = int(input("""
Escolha o tipo do investimento
 1.CDB 
 2.LCI 
 3.LCA 
 Digite o tipo do investimento (1,2 ou 3): """))

valor_bruto = float(input("Digite o valor a ser resgatado: R$ "))
dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

# Alíquota
if tipo == 1:
    nome = "CDB"
    if dias <= 180:
        aliquota = 22.5
    elif dias <= 360:
        aliquota = 20.0
    elif dias <= 720:
        aliquota = 17.5
    else:
        aliquota = 15.0
elif tipo == 2:
    nome = "LCI"
    aliquota = 0
else:
    nome = "LCA"
    aliquota = 0

imposto = valor_bruto * (aliquota/100)
valor_liquido = valor_bruto - imposto

# Saída de dados direta e organizada
print("\n--- RESUMO DO RESGATE ---")
print(f"Investimento: {nome}")
print(f"Valor Bruto: R$ {valor_bruto:.2f}")
print(f"Dias: {dias}")
print(f"Alíquota: {aliquota}%")
print(f"Imposto de Renda: R$ {imposto:.2f}")
print(f"Valor Líquido: R$ {valor_liquido:.2f}")
