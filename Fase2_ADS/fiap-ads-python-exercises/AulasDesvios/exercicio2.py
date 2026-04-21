#solicitando os dados do cliente
valor_compra = input("Informe o valor da compra realizada: ")
cupom = input("Digite o cupom de desconto: ")

#realizando teste logico
if cupom.upper() == "NIVER10":
    #caluclo de 10% de desconto
    valor_final = float(valor_compra) * 0.9
else:
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO")
#exibindo o valor final da compra
print(f"O valor final da compra é {valor_final:.2f}")