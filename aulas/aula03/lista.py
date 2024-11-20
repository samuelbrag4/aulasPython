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

# ---------- DECLARAÇÃO DE DADOS DE TIPOS DIFERENTES EM UMA LISTA

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

# ---------- LISTA DE LISTAS

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

# ---------- LISTA VAZIA

print("-----SEPARAÇÃO-----")

# Uma lista também pode ser vazia
lista_vazia = []

# Exibição da lista
print(lista_vazia)

# Exibiçãom do tipo da variável - "list"
print(type(lista_vazia))

# ---------- FUNÇÃO LEN()

print("-----SEPARAÇÃO-----")

# Contagem do tamanho de uma lista
print(len(frutas))
print("----------")
print(len(lista_vazia))

# ---------- PEGAR PEDAÇOS DA LISTA

print("-----SEPARAÇÃO-----")

print(a_lista)
print("\n")
# Pegar pedaços da lista - do início até o índice 2
print(a_lista[:2])
print("\n")
# Pegar pedaços da lista - do índice 2 até o final
print(a_lista[2:])
print("\n")
# Pegar pedaços da lista - do índice 2 até o índice 4
print(a_lista[2:4])

# ---------- INSERT()

print("-----SEPARAÇÃO-----")

'''
O método insert() adiciona um elemento em uma posição específica da lista.
Sintaxe: .insert(posição, elemento)
Exemplo:
'''

# Adicionar um elemento ao final da lista
frutas.insert(1, 'Abacaxi')

# Exibição da lista
print(frutas)

# ---------- APPEND()

print("-----SEPARAÇÃO-----")

# Para inserir valores no final da lista, pode-se usar o método append()
frutas.append("Laranja")

# Exibição da lista
print(frutas)

# ---------- EXTEEND()

print("-----SEPARAÇÃO-----")

# Para adicionar mais de um elemento ao final da lista, pode-se usar o método extend()
frutas.extend(["Limão", "Melancia", "Caju"])

# Exibição da lista
print(frutas)

# --- OU ---

# Lista de frutas adicionais
frutas_adicionais = ["Limão", "Melancia", "Caju"]

# Extentendo a lista de frutas com a lista de frutas adicionais
frutas.extend(frutas_adicionais)

# Exibição da lista
print(frutas)

'''
Explicação:
Por que usar o método extend() ao invés de append()?
O método .append() adiciona um elemento ao final da lista, de modo que neste caso, seria adicionada um lista dentro de uma lsta
Exemplo:
frutas.append(["Limão", "Melancia", "Caju"])
print(frutas)
Resultado:
['Banana', 'Maçã', 'Pera', 'Uva', 'Morango', 'Abacaxi', 'Laranja', 'Limão', 'Melancia', 'Caju', ['Limão', 'Melancia', 'Caju']]
Neste caso, foi adicionada uma lista dentro de outra lista.

Agora, o método .extend() adiciona os elementos da lista ao final da lista original, de modo que não haverá uma lista dentro de outra lista.
Exemplo:
frutas.extend(["Limão", "Melancia", "Caju"])
print(frutas)
Resultado:
['Banana', 'Maçã', 'Pera', 'Uva', 'Morango', 'Abacaxi', 'Laranja', 'Limão', 'Melancia', 'Caju', 'Limão', 'Melancia', 'Caju']
Neste caso, os elementos foram adicionados ao final da propria lista, sem criar outra com eles.
'''

# ---------- REMOVE()

print("-----SEPARAÇÃO-----")

# Remover um elemento da lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Removendo o terceiro elemento da lista
numeros.remove(3)

# Exibição da lista
print(numeros)

# ---------- POP()

print("-----SEPARAÇÃO-----")

# Remover um elemento da lista através do índice
numeros.pop(2)

# Exibição da lista
print(numeros)

'''
Explicação:
O método .pop() remove um elemento da lista atravéz de seu íncice. Se não foi passado nenhum índice, por padrão, o método remove o último elemento da lista
'''

# ----- OU

print(frutas)
fruta_removida = frutas.pop(2)
print(frutas)
print(fruta_removida)