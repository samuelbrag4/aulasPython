'''
1)Escreva um programa em Python para calcular o bônus de desempenho dos
funcionários de uma empresa com base em sua avaliação. O programa deve solicitar ao
usuário que insira a avaliação do funcionário (em uma escala de 1 a 5) e, em seguida,
calcular e imprimir o valor do bônus de acordo com as seguintes condições:

• Se a avaliação for 5, o bônus será de 20% do salário.
• Se a avaliação for 4, o bônus será de 15% do salário.
• Se a avaliação for 3, o bônus será de 10% do salário.
• Se a avaliação for 2, o bônus será de 5% do salário.
• Se a avaliação for 1, o funcionário não receberá nenhum bônus.
'''

avaliacao = int(input("Digite a avaliação do funcionário em uma escala de 1 a 5: "))

if avaliacao == 5:
    bonus = 0.20
elif avaliacao == 4:
    bonus = 0.15
elif avaliacao == 3:
    bonus = 0.10
elif avaliacao == 2:
    bonus = 0.05
else:
    bonus = 0
    
print(f"O bônus do funcionário será de {bonus*100}% do salário.")

'''
2)Escreva um programa em Python que classifique um número inteiro fornecido pelo
usuário em relação a zero. O programa deve imprimir uma mensagem indicando se o
número é positivo, negativo ou igual a zero.
'''

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é igual a zero.")

'''
3) Escreva um programa em Python para determinar se um cliente é elegível para um
empréstimo com base em sua renda mensal e na pontuação de crédito. O programa deve
solicitar ao usuário que insira sua renda mensal e sua pontuação de crédito. Em seguida,
deve aplicar as seguintes regras para decidir se o cliente é elegível:

• Se a renda mensal for superior a $5000 e a pontuação de crédito for maior ou igual a
700, o cliente é elegível para o empréstimo.
• Se a renda mensal for superior a $3000 e a pontuação de crédito for maior ou igual a
600, o cliente é elegível para o empréstimo, mas com uma taxa de juros mais alta.
• Se não atender a nenhum dos critérios acima, o cliente não é elegível para o empréstimo.
'''

renda_mensal = float(input("Digite a renda mensal do cliente: "))
pontuacao_credito = int(input("Digite a pontuação de crédito do cliente: "))

if renda_mensal > 5000 and pontuacao_credito >= 700:
    print("O cliente é elegível para o empréstimo!")
elif renda_mensal > 3000 and pontuacao_credito >= 600:
    print("O cliente é elegível para o empréstimo, mas com uma taxa de juros mais alta!")
else:
    print("O cliente não é elegível para o empréstimo!")