# Lambda em Python

'''
No Python, lambda é uma palavra-chave usada para criar funções anônimas, também conhecidas como funções
lambda. Essas funções são pequenas e geralmente usadas para operações simples. 

A sintaxe básica de uma função lambda é:

lambda argumentos: expressão

A função lambda pode ter vários argumentos, mas apenas uma expressão. A expressão é avaliada e retornada quando a função é chamada.

A função lambda é usada para criar funções temporárias e é usada em conjunto com funções de ordem superior, como map(), filter() e reduce().
'''

# Exemplo: Lambda
quadrado = lambda x: x ** 2

print(quadrado(2))

'''
Lamba - Filter

filter(funcao, sequencia)
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)

'''
Lamba - Map

map(função, sequência)
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ao_quadrado = list(map(lambda x: x ** 2, numeros))

print(ao_quadrado)

