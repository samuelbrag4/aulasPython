# MATRIZ - LISTA DE LISTAS

# Criando uma Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

'''
ESTRUTURA:

nomeMatriz = [
    [elemento1, elemento2, elemento3],
    [elemento4, elemento5, elemento6],
    [elemento7, elemento8, elemento9]
]

EXPLICAÇÃO:

- A Matriz é uma lista de listas
- Cada lista interna é uma linha da Matriz
- Cada elemento da lista interna é uma coluna da Matriz
'''

# Exibição da Matriz e do seu tipo
print(matriz)
print(type(matriz))

# EXIBIÇÃO DE UM OU MAIS ELEMENTOS DE UMA MATRIZ
print(matriz[0][0])
print(matriz[1][2])

'''
EXPLICAÇÃO:

- matriz[0] -> Acessa a primeira linha da Matriz
- matriz[0][0] -> Acessa o primeiro elemento da primeira linha da Matriz
- matriz[1][2] -> Acessa o terceiro elemento da segunda linha da Matriz
'''

# ALTERANDO VALORES DE ELEMENTOS DE UMA MATRIZ
matriz[0][0] = 10
matriz[1][1] = "Python"

'''
EXPLICAÇÃO:

- matriz[0][0] = 10 -> Altera o valor do primeiro elemento da primeira linha da Matriz para 10
- matriz[1][1] = "Python" -> Altera o valor do segundo elemento da segunda linha da Matriz para "Python"
'''

# Ebição da Matriz
print(matriz)