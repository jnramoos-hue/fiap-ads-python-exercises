# 'r' abrir para leitura (modo padrão)
# 'w' abrir para escrita
# 'a' abrir para escrita no final
# 'x' criar
# 't' texto
# 'b' abrir em modo binário
# '+' abrir para atualização


# Crindo uma variável com o texto
conteudo = "Há muito tempo em uma galáxia muit, muito distante..."

# Usando a função open para criar um objeto do tipo arquivo
# arquivo = open("/Users/junior/Desktop/Faculdade/Fase3_ADS/exercicios_python_json/arquivo_texto.txt", "w", encoding="utf-8")
#
# # Escrevendo o conteúdo na variável conteúdo dentro do arquivo em modo a
# arquivo.write(conteudo)

arquivo = open("/Users/junior/Desktop/Faculdade/Fase3_ADS/exercicios_python_json/arquivo_texto.txt", "a", encoding="utf-8")
arquivo.write("\nTeste novo ")


# Fechando o arquivo
arquivo.close()