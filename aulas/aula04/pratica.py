# Criar um dicionário de informações sobre uma pessoa e acessar alguns valores 

# Criar um dicionário com informações sobre uma pessoa
info_pessoa = {
    'nome': 'João',
    'idade': 25,
    'altura': 1.75,
    'peso': 70,
    'profissao': 'programador',
    'hobbies': ['ler', 'jogar', 'assistir filmes']
}

# Acessando valores do dicionário
print('Nome:', info_pessoa['nome'])
print('Idade:', info_pessoa['idade'])

# Variáveis para facilitar o acesso
nome = info_pessoa['nome']
idade = info_pessoa['idade']
profissao = info_pessoa['profissao']

# Print personalizado com f-strings
print(f'Altura: {info_pessoa["altura"]:.2f}')
print(f"{nome} tem {idade} anos e é {profissao}")