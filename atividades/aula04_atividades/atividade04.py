# 1) Considere o seguinte dicionário em Python: 

# Criação do dicionário
dicionario = {'idade': 25, 'nome': 'Ana'}

# Exibição
print(dicionario)

'''
Crie um programa que realiza a seguinte operação: 

Atualize o valor associado à chave 'idade' para 26. 

Ao executar o programa, o dicionário modificado deve ser impresso na tela. 
'''

# Atualização:
dicionario['idade'] = 26

# Exibição
print(dicionario)

# 2) Dado o seguinte dicionário em Python: 

# Criação do dicionário
dicionario = {'a': 1, 'b': 2, 'c': 3} 

# Exibição
print(dicionario)

'''
Desenvolva um programa que realize a seguinte operação: Remova a chave 'b' do dicionário.
'''

# Remoção
dicionario.pop('b')

# Exibição do novo dicionário
print(dicionario)