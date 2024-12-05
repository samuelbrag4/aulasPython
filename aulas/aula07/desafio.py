import random

'''
Crie um jogo em Python onde um usuário tem que adivinhar um número entre 1 e 5.
Utilize um loop de while com a declaração break para encerrar o jogo quando o usuário acertar.
Juntamente, coloque um contador de quantas tentativas foram realizadas para o usuário acertar o número.
'''

numero_alvo = random.randint(1, 5)

numero_usuario = int(input("Digite um número entre 1 e 5: "))

contador_tentativas = 0

while True:
    if numero_usuario == numero_alvo:
        print(f'Parabéns! Você acertou o número secreto, que era {numero_alvo}.')
        contador_tentativas += 1
        print(f'Você acertou em {contador_tentativas} tentativas.')
        break
    else:
        print('Você errou o número secreto! Continue tentando...')
        contador_tentativas += 1
        numero_usuario = int(input("Digite um número entre 1 e 5: "))
        
print('Fim do jogo.')