# Importando módilp JSON
import json

# Usando a função open para ler o arquivo JSON
arquivo = open("/Users/junior/Documents/GitHub/fiap-ads-python-exercises/Fase3_ADS/agenda.json", "r", encoding="utf-8")
# Colocando o conteudo do arquivo em uma variável  do tipo string
dicionario = json.loads(arquivo.read())
# Fechando o arquivo
arquivo.close()

# Usando o metodo loads para converter uma strings  no formato json em um dicionário
print(dicionario["Clark Kent"])
