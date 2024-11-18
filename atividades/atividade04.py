# Solicitação da inserção de uma frase
frase = input("Digite uma linguagem de programação que você gosta: ")

# Solicitação da inserção de uma nova linguagem
nova_palavra = input("Digite outra linguagem: ")

# Solicitação da inserção da linguagem que foi inserida anteriormente
antiga_palavra = input("Digite a linguagem que você inseriu anteriormente: ")

# Nova frase, que junta a frase inserida com a nova palavra
nova_frase = frase.replace(antiga_palavra, nova_palavra)

# Exibição 
print(f"A nova frase é: {nova_frase.capitalize()}")

'''
Uma forma mais fácil é só adicionar o valor da variável "nova_frase" dentro do print:
print(f"A nova frase é: {frase.replace(antiga_palavra, nova_palavra)}")

'''