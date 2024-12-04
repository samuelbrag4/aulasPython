# While 

'''
O arquivo "lacosRepeticoes" tem mais conteúdos que este, que serve somente para práticas
'''

# Exemplo01 --> Calculo do fatorial de um número (n!)
n = int(input("Digite um número: "))

resultado = 1
i = 1

while i <= n:
    resultado *= i
    i += 1
    
print(f'O fatorial do número inserido é {resultado}')

'''
Explicação do fluxo do código:

1. O dado inserido pelo usuário é armazenado na variável "n"
2. A variável "resultado" é inicializada com 1 e a variável "i" é inicializada com 1
3. while: enquanto o "i" for menor que o "n", o "resultado" será multiplicado pelo "i" e o "i" será incrementado em 1
4. O loop termina quando o "i" for maior que o "n"
5. O resultado é impresso na tela
'''

# Exemplo02 --> Loop de while que imprima números de 1 a 5 em ordem crescente
numero_usuario = int(input("Digite um número: "))

numero_sistema = 1

print('Iniciando a contagem...')

while numero_sistema <= numero_usuario:
    print(numero_sistema)
    numero_sistema += 1
    
print('Fim da contagem.')

# Exemplo03 --> Loop que calcula e imprime a soma dos números ímpares de 1 até um número inserido pelo usuário
numero_inserido = int(input("Digite um número: "))

soma = 0

contador = 1

while contador <= numero_inserido:
    if contador % 2 != 0:
        soma += contador
        contador += 1
    else:
        contador += 1
        
print(f'A soma dos números ímpares de 1 até {numero_inserido} é {soma}')