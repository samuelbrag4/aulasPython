'''
Pegue uma frase e conte quantas vogais e consoantes tem nela.
'''

vogais = ['a', 'e', 'i', 'o', 'u']

consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

totalVogais = 0

totalConsoantes = 0

frase = input('Digite uma frase: ')

palavras = frase.lower().split()

for palavra in palavras:
    for letra in palavra:
        if letra in vogais:
            totalVogais += 1
        elif letra in consoantes:
            totalConsoantes += 1
            
print(f'Vogais: {totalVogais}')
print(f'Consoantes: {totalConsoantes}')