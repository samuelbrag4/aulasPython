# Funções 

'''
Funções são blocos de código que podem ser chamados e executados em qualquer parte do programa.
Elas são definidas com a palavra reservada def seguida do nome da função e dos parênteses.

Estrutura de uma função:
def nome_da_funcao(parametros):
    bloco de código
    
Uma função pode ter vários parâmetros, ou não ter nenhum.

Chamando a função:
nome_da_funcao(argumentos)

Para chamar a função, basta escrever o nome da função seguido dos parênteses e dos argumentos que serão passados para a função.

Função com vários parametros: 
def nome_da_funcao(parametro1, parametro2, parametro3):
    bloco de código
    
Chamando a função com vários argumentos:
nome_da_funcao(argumento1, argumento2, argumento3)
'''

# Exempo01 --> Função que faz uma saudação
def saudacao(nome):
    print(f'Olá, {nome}!')
    
saudacao('João')

# Exemplo02 --> Função que soma dois números
def soma(a, b):
    return a + b

print(soma(3, 3))

# Exemplo03 --> Função que calcula a média de três números
def media(a, b, c):
    return (a + b + c) / 3

print(media(5, 1, 15))

# Exemplo04 --> Função que calcula a idade de uma pessoa com base no ano de nascimento e depois valida se ela já pode dirigir, seguido de uma veruficação se ela é maior de idade
def idade(ano_nacimento):
    idade = 2024 - ano_nacimento
    if idade >= 18:
        print('Você já pode dirigir! Pois é maior de idade!')
    else:
        print('Você ainda não pode dirigir! Pois é menor de idade!')
    return idade

print(idade(2000))

# Exemplo05 --> Função que verifica se um número é par ou ímpar
def numero_par_impar(numero):
    if numero % 2 == 0:
        print('O número é par!')
    else:
        print('O número é ímpar!')
        
numero_par_impar(5)

# Exemplo06 --> Função que fala qual dia é hoje

'''
Forma complicada:

hoje = 'segunda-feira'
print(f'Hoje é {hoje}!')

Forma mais simples utilizando função:
'''

def dia(dia):
    print(f'Hoje é {dia}!')
    
dia('segunda-feira')