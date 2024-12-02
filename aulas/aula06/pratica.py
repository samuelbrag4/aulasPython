'''
Faça um código que pergunte o valor de duas variáveis A e B (input)
Caso a variável A seja maior que B, exiba a mensagem "A é maior que B"
'''

# Solicitação de inserção dos dados:
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))

# Condicional:
if a > b:
    print('A é maior que B.')
else:
    print('B é maior que A.')
    
# Exibição final:
print(f'Valores inseridos: A = {a} e B = {b}.')