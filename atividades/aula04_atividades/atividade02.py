# Escreva um programa em Python que converta uma lista de caracteres em uma string.

# Criação da lista com as letras
lista = ["P", "Y", "T", "H", "O", "N"]

# Exibição da lista com as letras:
print(f"Esta é a lista inicial somente com as letras: {lista}.")

# Atualização da lista utilizando o .join()
string = "".join(lista)

# Exibição da string resultante:
print(f"Esta é a lista atualizada formando a palavra: {string}")

'''
EXPLICAÇÃO:

A lista inicial contém várias letras separadas. Para converter essa lista em uma string, utilizei o método ".join()". 
O método ".join()" é usado para concatenar todos os elementos de uma lista em uma única string. 
No exemplo, passei uma string vazia ("") como delimitador, o que significa que as letras serão unidas sem nenhum caractere entre elas.
O método ".join()" é muito útil para transformar listas de caracteres em strings de forma eficiente.
'''