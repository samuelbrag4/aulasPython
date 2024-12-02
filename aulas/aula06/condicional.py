# Operadores condicionais em Python

'''
Os comparadores de variáveis em python são:
    
        == : Igual a
        != : Diferente de
        > : Maior que
        < : Menor que
        >= : Maior ou igual a
        <= : Menor ou igual a
        
Eles ajudam a fazer operações 'booleanas' que retornam True ou False.
Comparando elementos e retornando True ou False.
'''

# Testes:

# Igual a:
print(2 == 2)

# Diferente de:
print(2 != 2)

# Maior que:
print(2 > 2)

# Menor que:
print(2 < 2)

# Maior ou igual a:
print(2 >= 2)

# Menor ou igual a:
print(2 <= 2)

print('\n-------------------\n')

'''
Operadores lógicos:

    and : E
    or : OU
    not : NÃO
    
Eles ajudam a fazer operações 'booleanas' que retornam True ou False.

and: Retorna True se ambos os valores forem True.
or: Retorna True se um dos valores for True.
not: Retorna True se o valor for False (inverte o valor).
'''

# Exemplos:

a = True
b = False

# and:
print(a and b)

# or:
print(a or b)

# not:
print(not a)
print(not b)

print('\n-------------------\n')
'''
CONDICIONAL --> IF

O if é uma estrutura condicional que permite avaliar uma expressão e, de acordo com o resultado, executar um bloco de código ou outro.

Ierarquia:

    if
    elif
    else
    
if: Se a condição for verdadeira, executa o bloco de código.
elif: Se a condição do if for falsa, ele testa a condição do elif.
else: Se todas as condições anteriores forem falsas, executa o bloco de código do else.

Sintaxe de ambos:

if condição:
    bloco de código
elif condição:
    bloco de código
else:
    bloco de código
'''

# Exemplo:
idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Voce tem a idade permitida.')
else:
    print('Voce tem menos que a idade permitida.')

# Exemplo com elif:
nota = float(input('Digite sua nota: '))

if nota >= 7:
    print('Aluno aprovado!')
elif nota >= 5:
    print('Aluno em processo de recuperação!')
else:
    print('Aluno reprovado!')