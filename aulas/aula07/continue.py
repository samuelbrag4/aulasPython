# Continue

'''
O continue é uma palavra reservada que faz com que o loop pule para a próxima iteração.
'''

i = 1

result = 1

while i < 20:
    i += 1
    if i % 2 == 0:
        print(f'Pular o número {i}')
        continue
    print(f'Multiplicando com {i}')
    result *= i
    
print(f'i: {i} \nresultado: {result}')