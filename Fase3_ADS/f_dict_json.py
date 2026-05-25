# Criando um dicionário em JSON
import json
contatos = {
    "Clark Kent":
        {"Celular": "99999-9999",
        "E-mail": "super@krypton.com"},
    "Bruce Wayne":
        {"Celular": "88888-8888",
         "E-mail": "bat@caverna.com.br"}
}

# Convertendo o dicionário para uma string em formato JSON
conteudo_string = json.dumps(contatos, indent=4, ensure_ascii=False)

# Criando um arquivo JSON
arquivo = open("/Users/junior/Documents/GitHub/fiap-ads-python-exercises/Fase3_ADS/agenda.json", "w", encoding="utf-8")

# Escrevendo o JSON dentro do arquivo
arquivo.write(json.dumps(contatos, indent=4, ensure_ascii=False))

# Fechando o arquivo
arquivo.close()

