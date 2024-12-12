import random # A gente vai usar isso pra gerar um número aleatório

# Função principal do jogo
def jogar_adivinhacao():
    print("=== Jogo de Adivinhação ===")
    # Pedimos o nome do jogador logo de cara
    nome_jogador = input("Digite seu nome: ")
    jogar_novamente = True # Variável pra saber se o jogador quer continuar jogando

    while jogar_novamente: # Esse loop mantém o jogo rolando enquanto o jogador quiser
        # Aqui geramos um número secreto entre 1 e 5
        numero_secreto = random.randint(1, 5)
        tentativas = 0 # Conta quantas vezes o jogador tentou
        acertou = False # Controla se o jogador acertou ou não

        print("\nBeleza, o número foi gerado. Agora tente adivinhar um número entre 1 e 5!")

        while not acertou: # Enquanto o jogador não acertar, o jogo continua pedindo palpites
            try:
                # Pedimos o palpite e garantimos que é um número
                palpite = int(input("Qual o seu palpite? "))
                tentativas += 1 # Cada palpite conta como uma tentativa

                # Se o jogador acertar, a gente comemora!
                if palpite == numero_secreto:
                    acertou = True # Sai do loop
                    print(f"Boa, {nome_jogador}! Você acertou o número em {tentativas} tentativa(s).")

                    # Salva o nome e as tentativas no arquivo
                    with open("resultados_jogo.txt", "a") as arquivo:
                        arquivo.write(f"{nome_jogador} - {tentativas} tentativa(s)\n")
                else:
                    print("Errado! Tenta de novo.") # Dá um feedback e deixa o jogo rolar
            except ValueError:
                # Se o jogador digitar qualquer coisa que não seja número, avisamos
                print("Ops! Por favor, insira um número válido.")

        # Depois que acertar, perguntamos se quer jogar outra vez
        resposta = input("\nQuer jogar de novo? (sim/não): ").strip().lower()
        if resposta != "sim":
            # Se não quiser jogar de novo, agradecemos e saímos do loop
            jogar_novamente = False
            print("Valeu por jogar! Até a próxima!")

# Aqui começa tudo: chamamos a função principal pra iniciar o jogo
jogar_adivinhacao() 