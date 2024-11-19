# Criando uma Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Exibição da Matriz
print(matriz)

# Exibição do tipo da MAtriz
print(type(matriz))

'''
Basicamente, uma matriz é uma lista de listas. 
'''

# Exibição de um (ou mais) elemento(s) da Matriz
print(matriz[0][0])
print(matriz[1][2])

# ----------

print("-----SEPARAÇÃO-----")

# Alterar o valor de um elemento da Matriz
matriz[0][0] = 10
matriz[1][1] = "Python"

# Ebição da Matriz
print(matriz)
