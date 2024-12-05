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