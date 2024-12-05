# Loop de --- for ---

'''
O loop de for é um loop que é utilizado quando se sabe a quantidade de vezes que o loop deve ser executado.
O loop de for é composto por três partes:
    1. A palavra reservada "for"
    2. Uma variável que será utilizada para iterar sobre um objeto iterável
    3. O objeto iterável que será percorrido
    
Sintaxe:

for variavel in objeto_iteravel:
    bloco de código
'''

# Exemplo01 --> Lista de dias
dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']

for dia in dias:
    print(dia)
    
# Exemplo02 --> Lista de letras em uma string
frase = input('Digite uma frase: ')

for char in frase:
    print(char)
    
# Exemplo03 --> Loop sobre uma tupla
tupla = ('uva', 'maçã', 'banana', 'laranja', 'manga')

for numero in tupla:
    print(f'Eu gosto de {numero}')
    
# Exemplo04 --> Loop sobre um dicionário
dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}

for chave in dicionario:
    print(f'{chave}: {dicionario[chave]}')
    
# Exemplo05 --> Loop sobre um range

for i in range(10):
    print(i)
    
# ou

for i in range(3, 10):
    print(i)
    
# Começa do 3 e vai até o 10

# OU

for i in range(3, 10, 4):
    print(i)
    
# Começa do 3 e vai até o 10 pulando de 4 em 4

# Exemplo06 

for i in range(len(dias)):
    print(f'O valor na posição {i} é {dias[i]}')
    
# Exemplo07 
persons = [{'name': 'João', 'age': 25}, {'name': 'Maria', 'age': 30}, {'name': 'José', 'age': 35}]

for person in persons:
    for key in person:
        print(f'{key}: {person[key]}')
    print(' ')

# Prática --> impressão de números de 1 a 5 em ordem crescente 
for i in range(1, 6):
    print(i)
    
# Prátoca --> O usuário irá inserir um número e a tabuada dele até 10 deve ser impressa
numero = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{numero} X {i} = {numero * i}')