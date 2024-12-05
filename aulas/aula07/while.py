# # While 

# '''
# O arquivo "lacosRepeticoes" tem mais conteúdos que este, que serve somente para práticas
# '''

# # Exemplo01 --> Calculo do fatorial de um número (n!)
# n = int(input("Digite um número para calcularmos o seu fatorial: "))

# resultado = 1
# i = 1

# while i <= n:
#     resultado *= i
#     i += 1
    
# print(f'O fatorial do número inserido é {resultado}')

# '''
# Explicação do fluxo do código:

# 1. O dado inserido pelo usuário é armazenado na variável "n"
# 2. A variável "resultado" é inicializada com 1 e a variável "i" é inicializada com 1
# 3. while: enquanto o "i" for menor que o "n", o "resultado" será multiplicado pelo "i" e o "i" será incrementado em 1
# 4. O loop termina quando o "i" for maior que o "n"
# 5. O resultado é impresso na tela
# '''

# # Exemplo02 --> Loop de while que imprima números de 1 a 5 em ordem crescente
# numero_usuario = int(input("Digite um número para vermos a contagem dele: "))

# numero_sistema = 1

# print('Iniciando a contagem...')

# while numero_sistema <= numero_usuario:
#     print(numero_sistema)
#     numero_sistema += 1
    
# print('Fim da contagem.')

# # Exemplo03 --> Loop que calcula e imprime a soma dos números ímpares de 1 até um número inserido pelo usuário
# numero_inserido = int(input("Digite um número para vermos a soma dos impares de 1 até ele: "))

# soma = 0

# contador = 1

# while contador <= numero_inserido:
#     if contador % 2 != 0:
#         soma += contador
#         contador += 1
#     else:
#         contador += 1
        
# print(f'A soma dos números ímpares de 1 até {numero_inserido} é {soma}')

# '''
# Explicação do fluxo do código:

# 1. O dado é inserido pelo usuário e armazenado na variável "numero_inserido"
# 2. A variável "soma" é inicializada com 0 e a variável "contador" é inicializada com 1
# 3. O loop de while faz a segunte condição: 
#     enquanto o contador for menor ou igual ao número inserido pelo usuário, um if é executado, que faz e seguinte condição:
#         se o resto da divisão do contador por 2 for diferente de 0 (impar), a variável "soma" é incrementada com o valor do contador e o contador é incrementado em 1
#         senão, o contador é incrementado em 1
# 4. O loop termina quando o contador for maior que o número inserido pelo usuário
# 5. A soma dos números ímpares é mostrada
# '''

# # Exemplo04 --> Loop que exiba a tabuada de um número inserido pelo usuário. Indo de 1 a 10
# numero_tabuada = int(input("Digite um número para vermos a tabuada dele: "))

# multiplicador = 1

# while multiplicador <= 10: 
#     print(f'{numero_tabuada} x {multiplicador} = {numero_tabuada * multiplicador}')
#     multiplicador += 1
    
'''
Explicação do fluxo do código:

1. O dado é inserido pelo usuário e armazenado na variável "numero_tabuada"
2. A variável "contador" é inicializada com 1
3. O loop de while faz a seguinte condição:
    enquanto o contador for menor ou igual a 10, o print é executado mostrando a tabuada do número inserido pelo usuário
4. O contador é incrementado em 1
5. O loop termina quando o contador for maior que 10
'''

# Exemplo05 --> Loop que conte de 1 até 10, mas que pule os números 3 e 7. Utilizando o continue
contagem = int(input("Digite um número para vermos a contagem dele: "))

contador_contagem = 1

while contador_contagem <= contagem:
    if contador_contagem == 3 or contador_contagem == 7:
        contador_contagem += 1
        continue
    print(contador_contagem)
    contador_contagem += 1


'''
Explicação do fluxo do código:

1. O dado é inserido pelo usuário e armazenado na variável "contagem"
2. A variável "contador_contagem" é inicializada com 1
3. O loop de while faz a seguinte condição:
    enquanto o contador_contagem for menor ou igual a contagem, um if é executado, que faz a seguinte condição:
        se o contador_contagem for igual a 3 ou igual a 7, o contador_contagem é incrementado em 1 e o continue
        senão, o print é executado mostrando a contagem
4. O contador_contagem é incrementado em 1
5. O loop termina quando o contador_contagem for maior que a contagem
'''

