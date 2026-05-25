import configparser
import os


config = configparser.ConfigParser()
config_file = "/Users/junior/Documents/GitHub/fiap-ads-python-exercises/Fase3_ADS/config.ini"

if not os.path.exists(config_file):
    raise FileExistsError(f"The configuraion file {config_file} does not exists.")

# Lê o arquivo de configuração
config.read(config_file)

# Exibindo o c tipo do objeto config
print(type(config))

# Acesando as configurações
print(config["general"]["app_name"])

# Exibindo todas as configs.sections e as confit.intems(section) com loop
for secao in config.sections():
    print(secao)
    for chave, valor in config.items(secao):
        print(f"{chave} - {valor}")

