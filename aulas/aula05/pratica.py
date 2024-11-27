print("---PRATICA 01---")
# Escreva um programa em Python para criar uma tupla com diferentes tipos de dados.

# Criando uma tupla com diferentes tipos de dados
tupla = (1, 'Python', 3.14, True, 'Java', 2.71, False, 'C++', 0.0, 'C#', 0, 'Next')

# Exibindo a tupla
print(tupla)

print("---PRATICA 02---")

'''
Escreva um programa em Python que crie uma tupla

fruta = ('Banana', 'Maçã', 'Uva')

Insira um novo item sem apagar a tupla original.
'''

# Criação da tupla
fruta = ('Banana', 'Maçã', 'Uva')

# Exibição dela e de seu tipo
print(f"Esta é a tupla: {fruta} \n Este é o tipo da tupla: {type(fruta)}")

# Transformando a tupla em lista para adicionar um novo item
fruta = list(fruta)

# Exibindo a lista
print(f"Esta é a lista: {fruta} \n Este é o tipo da lista: {type(fruta)}")

# Adicionando um novo item
fruta.append('Tomate')

# Exibindo a lista com a nova fruta
print(f"Esta é a lista com a nova fruta: {fruta}")

# Transformando a lista em tupla novamente
fruta = tuple(fruta)

# Exibindo a nova tupla
print(f"Esta é a nova tupla: {fruta} \n Este é o tipo da nova tupla: {type(fruta)}")

# OUTRA FORMA DE FAZER - ERRADA

# Adicionando um novo item
fruta = fruta + ('Lichia', 'Morango')

# Exibindo a nova tupla
print(fruta)