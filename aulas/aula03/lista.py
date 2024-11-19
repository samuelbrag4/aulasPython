'''
Uma lista é uma coleção de itens em uma ordem particular.
A lista deve ser declarada/criada dentro de colchetes([]), e os elementos dela devem ser separados por vírgula.
Segue um exemplo de declaração de uma lista de frutas:
'''

# Declaração de uma lista
frutas = ["Banana", "Maçã", "Pera", "Uva", "Morango"]

# Exibição da lista
print(frutas)

#Exibiçãom do tipo da variável - "list"
print(type(frutas))

# Acessando elementos da lista através de índices
print(frutas[0])
print("----------")
print(frutas[1])

# ----------

print("-----SEPARAÇÃO-----")

# Declarar outros tipos de dados em uma lista

'''
Na lista podem ser armazenados diferentes tipos de dados, como inteiros, strings, booleanos, floats, etc.
Pode-se declarar em uma lista diferentes tipos de dados, que tem funções completamente diferentes. Como por exemplo, armazenar um texto e a soma de dois números.
Segue exemplos:
'''

a_lista = ["Banana", 1, 2.5, True, "Nome", 4==4, 1 + 2]

# Exibição da lista
print(a_lista)

# Exibiçãom do tipo da variável - "list"
print(type(a_lista))

# ----------

print("-----SEPARAÇÃO-----")

'''
Em uma lista, você pode armazenar outras listas, juntamente de outros tipos de dados. NÃO HÁ LIMITESSSSSS
Exemplo:
'''

# Declaração de uma lista
lista1 = [a_lista, frutas, "Python", None, 3.14, 10 / 2, 3 <= 5]

# Exibição da lista
print(lista1)

# Exibiçãom do tipo da variável - "list"
print(type(lista1))

# Exemplo de acesso à valores da lista
print(lista1[1])

print("-----SEPARAÇÃO-----")

# Exemplo de acesso à valores da lista que está dentro de outra lista
print(lista1[1][1])
'''
Explicação:
Eu entro na lista1 e pego o índice 1, que é a lista de frutas. Depois, entro na lista de frutas e pego o índice 1, que é a maçã.
'''

# ----------

print("-----SEPARAÇÃO-----")

# Uma lista também pode ser vazia
lista_vazia = []

# Exibição da lista
print(lista_vazia)

# Exibiçãom do tipo da variável - "list"
print(type(lista_vazia))

# ----------

print("-----SEPARAÇÃO-----")

# Contagem do tamanho de uma lista
print(len(frutas))
print("----------")
print(len(lista_vazia))
