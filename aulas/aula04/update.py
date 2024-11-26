# Método update() para atualizar um dicionário

# Criação do dicionário
dict1 = {
    "a": 10,
    "b": 1,
    "c": 2
}

# Exibição
print(dict1)

# Utilizando o método update()
dict1.update({"b": 5})

# Nova exibição
print(dict1)

# Utilizando ele para incluir uma chave nova
dict1.update({"d": 7})

# Nova exibição
print(dict1)

# Outra forma de fazer

# Dicionário original 
dicionario1 = {
    "a": 10,
    "b": 1,
    "c": 2
}

# Exibir
print(dicionario1)

# Dicionário que será adicionado
dicionario2 = {
    "b": 5,
    "d": 7
}

# Adicona elementos de outro dicionário
dicionario1.update(dicionario2)

# Exibir
print(dicionario1)