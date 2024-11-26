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