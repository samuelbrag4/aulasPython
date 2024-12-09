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