# Dicionário 

# Criação do dicionário
meus_dados = {
    "nome": "Samuel",
    "Idade": 16,
    "Programa": True
}

# Exibição do dicionário
print(meus_dados)

# Exibição do tipo
print(type(meus_dados))

# OUTRA FORMA 

persona = dict(nome="Maria", sexo="Feminino", idade=28, casado=True)

print(persona)
print(type(persona))

print(f"O nome é: {persona["nome"]}, do sexo: {persona["sexo"]}")

# Dicionário vasio e adicionando valores nele

# Declaração do dicionário
dict1 = {}

# Exibição dele
print(dict1)

# Adicionando um dado ao dicionário vazio
dict1["chave1"] = "Não está mais vazio!!"

# Novo dicionário 
print(dict1)

# Lista junto com o dicionário

# Criação do dicionário com a lista
dict2 = {
    "Pessoa01": ["william", 30, "Professor"],
    "Pessoa02": ["Julia", 50, "Médica"]
}

# Exibição dele
print(dict2)

# Exibição do tipo
print(type(dict2))

# Acessando elemento dele
print(dict2["Pessoa02"][0])

# Dicionário dentro de um dicionário

pessoa = {
    "nome": "Samuel",
    "idade": 16,
    "enderco": {
        "rua": "Tal",
        "cidade": "Tal Tal",
        "estado": "Tal Tal Tal"
    }
}

# Exibição
print(pessoa)

# Acessando dados
print("Idade:", pessoa["idade"])
print("Endereço", pessoa["enderco"]["rua"], pessoa["enderco"]["cidade"])

# Alterar informações
pessoa["idade"] = 17
pessoa["enderco"]["rua"] = "Rua Tal Tal"

# Exibição
print(pessoa)
print(type(pessoa))
