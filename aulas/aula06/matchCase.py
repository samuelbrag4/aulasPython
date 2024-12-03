# Match Case

'''
Match Case é uma nova funcionalidade do Python 3.10 que permite a comparação de valores de uma variável com múltiplos valores de uma forma mais legível e eficiente.
Ele é praticamente uma estrutura condicional que permite comparar valores de uma variável com múltiplos valores. Muito parecido com um if-elif-else, mas com uma sintaxe 
mais limpa e legível.

Sintaxe:

match variável:
    case valor1:
        # código
    case valor2:
        # código
    case valor3:
        # código
    case _:
        # código
'''

# Solicitação dos dados:
idade_usuario = int(input('Digite sua idade: '))

# Condição usando match-case:
match idade_usuario:
    case idade if idade <= 17:
        print(f'A sua idade é {idade_usuario}. Desta forma, você é uma Criança/Adolescente.')
    case idade if idade <= 65:
        print(f'A sua idade é {idade_usuario}. Desta forma, você é um Adulto.')
    case idade if idade <= 100:
        print(f'A sua idade é {idade_usuario}. Desta forma, você é um Idoso.')
    case _:
        print(f'A sua idade é {idade_usuario}. Desta forma, você é um Morto vivo.')