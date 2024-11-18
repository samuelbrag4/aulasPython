# Método callable()
# Retorna True se o objeto parecer chamável (como uma função).
# Exemplo:
def funcao():
    pass
print(callable(funcao))  # Saída: True

# Método id()
# Retorna o "identificador" de um objeto.
# Exemplo:
objeto = "Python"
print(id(objeto))  # Saída: (um número inteiro único)

# Método isinstance()
# Verifica se um objeto é uma instância ou subclasse de uma classe.
# Exemplo:
print(isinstance(5, int))  # Saída: True

# Método type()
# Retorna o tipo do objeto.
# Exemplo:
print(type(5))  # Saída: <class 'int'>

# Método zip()
# Junta dois ou mais iteráveis em um iterável de tuplas.
# Exemplo:
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
print(list(zip(lista1, lista2)))  # Saída: [(1, 'a'), (2, 'b'), (3, 'c')]