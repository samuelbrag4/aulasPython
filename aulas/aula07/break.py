# Break

'''
O comando break é utilizado para interromper a execução de um loop.
'''

# Exemplo: Loop que calcula o fatorial de um número e interrompe a execução do loop quando o resultado for 42
i = 1

result = 1

while i <= 100:
    result *= i
    if i == 42:
        print('Chegou no 42! Parar a execução.')
        break
    i += 1
    
print(f'i: {i} \nresultado: {result}')