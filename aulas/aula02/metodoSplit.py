frase = "A segunda acabou"

print(frase)
print(type(frase))

# O método split() divide a string em uma lista de strings, separando-as por espaços em branco
frase_split = frase.split()
print(frase_split)
print(type(frase_split))

# Teste

nome = "Samuel dos Santos Braga"

# O split() sem argumentos divide a string por espaços em branco, sem a necessidade de passar o espaço como argumento
nome_list = nome.split(" ")

print(nome_list)

first_name = nome_list[0]

print(first_name)

# Teste 2

frase = "      A segunda acabou"

print(frase)
print(type(frase))
frase_split = frase.split()
print(frase_split)
print(type(frase_split))
print("----------") # Somente para divisão dos resultados

# Remover o espaço no início e no final
frase_strip = frase.strip()
print(frase_strip)
frase_split = frase_strip.split(" ")
print(frase_split)
print(type(frase_split))