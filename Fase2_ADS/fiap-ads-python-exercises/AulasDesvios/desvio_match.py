numero_combo = int(input("Digite o número do combo: "))

match numero_combo:
    case 1:
        nome_prato = "Hamburguer"
        valor_prato = 12.50
    case 2:
        nome_prato = "Cheseburguer"
        valor_prato = 15.00
    case 3:
        nome_prato = "X-Bacon"
        valor_prato = 17.00
    case _:
        nome_prato = None
        valor_prato = None

if nome_prato:
    print(f"O lanche escolhido é o {nome_prato} e o valor do combo é R${valor_prato}.")