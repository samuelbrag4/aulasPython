'''
O Python permite que você acesse os elementos de uma string através de índices.
Os indices começa a partir do 0, ou seja, o primeiro elemento é o 0, o segundo é o 1 e assim por diante.
'''

# Declarar uma String
dia_semana = "Segunda"

# Pega o "S" - primeira letra
print(dia_semana[0])

# Pega o "A" - acessa o elemento que vem antes do "S", que como não tem, vai para o final, pegando o "A"
print(dia_semana[-1])

# Pega uma quantidade maior (no caso as letras que começam no índice 0 e termina no 4)
print(dia_semana[0:4])