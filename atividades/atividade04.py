# Solicitação da inserção de uma frase
frase = input("Digite uma linguagem de programação que você gosta: ")

nova_palavra = input("Digite outra linguagem: ")

antiga_palavra = input("Digite a linguagem que você inseriu anteriormente: ")

nova_frase = frase.replace(antiga_palavra, nova_palavra)

print(f"A nova frase é: {nova_frase.capitalize()}")