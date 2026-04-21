#Verificar se os batimentos cardiacos estão na faixa adequada. Para isso, voce deve solicitar ao usuário informe o seu NUMERO DE BATIMENTOS POR MINUTO (BPM) e a IDADE. A partir disso o script deva verificar e enviar uma mensagem informando se os batimentos do usuário encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada ou ABAIXO da faixa adequada de acordo com o site a tua saude (https://www.tuasaude.com/frequencia-cardiaca/#:~:text=At%C3%A9%202%20anos%20de%20idade,idosos%3A%2050%20a%2060%20bpm)

# IDADE|______________________| BMP

# ATE 2 ANOS                  - 120 ATÉ a 140
# DE 8 ANOS ATÉ 17 ANOS       - 80 a 100
# ADULTO SEDENTÁRIO           - 70 A 80
# IDOSOS                      - 50 A 60

print("""
__________________________________
VERIFICADOR DE FREQUÊNCIA CARDIACA.
__________________________________
""")

idade = int(input("Por favor, informe a sua IDADE: "))
bpm = int(input("Por favor, informe os seus BATIMENTOS POR MINUTO (BPM): "))

if idade <= 2:
    if bpm >= 120:
        if bpm <= 140:
            print("Batimentos NORMAIS para a idade fornecida.")
        else:
            print("Batimentos ACIMA dos indicados para idade.")
    else:
        print("Batimentos ABAIXO dos indicados para idade.")
elif idade >= 8:
    if idade <= 17:
        if bpm >= 80:
            if bpm <= 100:
                print("Batimentos NORMAIS para a idade fornecida.")
            else:
                print("Batimentos ACIMA dos indicados para idade.")
        else:
            print("Batimentos ABAIXO dos indicados para idade.")
    if idade  >= 18:
        if idade <= 60:
            if bpm >= 70:
                if bpm <= 80:
                    print("Batimentos NORMAIS para a idade fornecida.")
                else:
                    print("Batimentos ACIMA dos indicados para idade.")
            else:
                print("Batimentos ABAIXO dos indicados para idade.")
        else:
            if bpm >= 50:
                if bpm <= 60:
                    print("Batimentos NORMAIS para a idade fornecida.")
                else:
                    print("Batimentos ACIMA dos indicados para idade.")
            else:
                print("Batimentos ABAIXO dos indicados para idade.")






