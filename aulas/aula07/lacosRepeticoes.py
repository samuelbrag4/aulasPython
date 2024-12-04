# Laços de repetição

'''
Tipos de laços de repetição:

1. while
2. for

__ While __

while condicao:
    bloco de código

__ For __

for variavel in sequencia:
    bloco de código

O que cada um faz?

1. while: executa um bloco de código enquanto a condição for verdadeira. É utilizado para quando não sabemos quantas vezes o bloco de código será executado.

2. for: executa um bloco de código para cada elemento de uma sequência. É utilizado quando sabemos quantas vezes o bloco de código será executado.
'''

# Exemplo de while - Uma idade é fornecida, até que ela seja maior que 18, o programa adiciona mai um a idade e exibe mensagens enquanto isso acontece 
idade = 0

while idade < 18:
    print('Você não pode dirigir')
    idade = idade + 1

print('Você já pode dirigir')

# Exemplo de for - Uma lista de nomes é fornecida, o programa exibe cada nome da lista
nomes = ['Ana', 'Maria', 'João', 'Pedro']

for nome in nomes:
    print(nome)

