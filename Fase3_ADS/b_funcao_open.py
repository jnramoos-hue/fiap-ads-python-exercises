#Usando a função open para criar um objeto do tipo arquivo
arquivo = open("/Users/junior/Desktop/Faculdade/Fase3_ADS/exercicios_python_json/arquivo.txt", "r", encoding="utf-8")
print(type(arquivo))
print(arquivo)
print(arquivo.read())
