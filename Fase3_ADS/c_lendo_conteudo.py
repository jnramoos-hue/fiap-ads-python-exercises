#Usando a função open para criar um objeto do tipo arquivo
arquivo = open("/Users/junior/Desktop/Faculdade/Fase3_ADS/exercicios_python_json/arquivo.txt", "r", encoding="utf-8")

#printando o conteúdo do arquivo
# print(arquivo.read())

# Printando uma linha do arquivo
# print(arquivo.readline())
#
# Printando outra linha do arquivo
# print(arquivo.readline())

# Passando o conteúdo do arquivo para uma lista
lista_linhas = arquivo.readlines()
print(lista_linhas)

# Comprovando o tipo do objeto linhas_do_arquivo
print(type(lista_linhas))

# Colocando a lista em ordem alfabética
lista_linhas.sort()
print(lista_linhas)

# Exibindo uma linha por vez, utilizando o loop for e o metodo readline()
for linha in lista_linhas:
    print(linha)

#fechando o arquivo
arquivo.close()
