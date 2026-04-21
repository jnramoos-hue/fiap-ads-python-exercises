import math
#solicitando os valores de A, B e C
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

#CALCULO DO DELTA
delta = b ** 2 - 4 * a * c
#Verificação das condições com elif
if delta > 0.0:
    # Calculo dos 2 valores de x
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Para a equação {a}x² + {b}x + {c} = 0 , obtivemos os seguintes valores: {x1} e {x2}")
elif delta == 0.0:
    #calculo de 1 valor para X
    x = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Para a equação {a}x² + {b}x + {c} = 0, obtivemos os seguintes valores: {x}")
else:
    print(f"Para a equação {a}x² + {b}x + {c} = 0, não existem valores reais para x.")