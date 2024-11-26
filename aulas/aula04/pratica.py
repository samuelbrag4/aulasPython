# Criar um dicionário de informações sobre uma pessoa e acessar alguns valores 

# Criar um dicionário com informações sobre uma pessoa
info_pessoa = {
    "nome": "João",
    "idade": 25,
    "altura": 1.75,
    "peso": 70,
    "profissao": "programador",
    "hobbies": ["ler", "jogar", "assistir filmes"]
}

# Acessando valores do dicionário
print("Nome:", info_pessoa["nome"])
print("Idade:", info_pessoa["idade"])

# Variáveis para facilitar o acesso
nome = info_pessoa["nome"]
idade = info_pessoa["idade"]
profissao = info_pessoa["profissao"]

# Print personalizado com f-strings
print(f"Altura: {info_pessoa['altura']:.2f}")
print(f"{nome} tem {idade} anos e é {profissao}")

# Criar um dicionário de estoque de produtos e atualize a quantidade de alguns itens

# Dicionário de estoque
estoque = {
    "banana": 10,
    "maçã": 5,
    "laranja": 7,
    "uva": 15
}

# Exibição
print(estoque)

# Atualizar quantidade de alguns itens
estoque["banana"] = 15
estoque["maçã"] += 10
estoque["laranja"] -= 3

# Novo estoque
print(estoque)

# Crie um dicionário de alunos e remova um utilizando o método pop()

# Dicionário de alunos
alunos = {
    "João": 8.5,
    "Maria": 2,
    "Pedro": 10,
    "Ana": 4
}

# Exibição
print(alunos)

# Remoção de um aluno
aluno_removido = alunos.pop("Pedro")

# Exibição do aluno removido
print(f"Aluno removido: {aluno_removido}")

# Novo dicionário
print(alunos)