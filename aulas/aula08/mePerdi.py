numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ao_quadrado = list(map(lambda x: x ** 2, numeros))

print(ao_quadrado)

'''
Lambda:

- Função anônima
- Não precisa de nome
- Pode ter vários argumentos
- Pode ter várias linhas de código
- Pode ser atribuída a uma variável

Sintaxe:
lambda argumentos: expressão
'''

# Exemplo: Lambda
quadrado = lambda x: x ** 2

print(quadrado(2))

# Lambda - Filter
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)