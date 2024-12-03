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
