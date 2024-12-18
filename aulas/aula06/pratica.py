'''
Faça um código que pergunte o valor de duas variáveis A e B (input)
Caso a variável A seja maior que B, exiba a mensagem "A é maior que B"
'''

# Solicitação de inserção dos dados:
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))

# Condicional:
if a > b:
    print('A é maior que B.')
else:
    print('B é maior que A.')
    
# Exibição final:
print(f'Valores inseridos: A = {a} e B = {b}.')

# Prática com elif:
nota = float(input('Digite sua nota: '))

if nota >= 7:
    print('Aluno aprovado!')
elif nota >= 5:
    print('Aluno em processo de recuperação!')
else:
    print('Aluno reprovado!')
    
# Pática que PARECE ser dificil:
'''
Faça um código que pergunte o valor de duas variáveis A e B (input)
Caso a variável A seja maior que B, exiba a mensagem "A é maior que B"
Caso a variável B seja maior que A, exiba a mensagem "B é maior que A"
Também verifique se A é duas vezes maior que B, exiba a mensagem "A é duas vezes maior que B"
'''

# Solicitação de inserção dos dados:
A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))

# Condição:
if A < B:
    print('B é maior que A.')
elif A == 2 * B:
    print('A é o dobro de B.')
else:
    print('A é maior que B.')
    
# OU

if (A / B) == 2:
    print('A é o dobro de B.')
elif A > B:
    print('A é maior que B.')
else:
    print('B é maior que A.')
    
'''
Faça um código para verificar se um número é par ou ímpar.
'''

# Solicitação de inserção dos dados:
num = int(input('Digite um número: '))

# Condição:
if num % 2 == 0:
    print('Número par.')
else:
    print('Número ímpar.')


'''
Solicite a idade de um usuário e verifique se ele é maior de idade.
'''

# Solicitação de inserção dos dados:
idade = int(input('Digite sua idade: '))

# Condição:
if idade >= 18:
    print('Você é maior de idade :D')
else:
    print('Você é menor de idade :C')
    
'''
Solicite a nota de um aluno e verifique se suas notas são A, B, C ou D.
'''

# Solicitação de inserção dos dados:
nota = float(input('Digite sua nota: '))

# Condição:
if nota >= 9:
    print('Nota A! Aluno aprovado!')
elif nota >= 7:
    print('Nota B! Aluno aprovado!')
elif nota >= 5:
    print('Nota C! Aluno em recuperação!')
else:
    print('Nota D! Aluno reprovado!')
    
'''
Solicite um número e verifique se ele é positivo, negativo ou zero. e imprima uma mensagem correspondente.
'''

# Solicitação de inserção dos dados:
numero = float(input('Digite um número: '))

# Condição:
if numero > 0:
    print('Número positivo.')
elif numero < 0:
    print('Número negativo.')
else: 
    print('Número zero.')
    
'''
Solicite a idade do usuário e escreva um programa em Python que verifique a categoria da idade
Considere as seguintes categorias:

- Criança/Adolescente --> 0 a 17 anos
- Adulto --> 18 a 65 anos
- Idoso --> 66 a 100
- Morto vivo --> 101 anos ou mais
'''

# Solicitação dos dados:
idade_usuario = int(input('Digite sua idade: '))

# Condição:
if idade_usuario <= 17:
    print(f'A sua idade é {idade_usuario}. Desta forma, você é uma Criança/Adolescente.')
elif idade_usuario <= 65:
    print(f'A sua idade é {idade_usuario}. Desta forma, você é um Adulto.')
elif idade_usuario <= 100:
    print(f'A sua idade é {idade_usuario}. Desta forma, você é um Idoso.')
else:
    print(f'A sua idade é {idade_usuario}. Desta forma, você é um Morto vivo.')