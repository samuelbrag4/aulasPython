# DICIONÁRIO, uma forma de armazenar dados de forma mais organizada

# Criação de um dicionário
meus_dados = {
    "nome": "Samuel",
    "Idade": 16,
    "Programa": True
}

'''
ESTRUTURA:

nomeDicionario = {
    "chave": "valor"
}

OU - com mais de um valor

nomeDicionario = {
    "chave1": "valor1",
    "chave2": "valor2",
    "chave3": "valor3"
}

Ou seja, um dicionário é composto por chaves e valores, onde as chaves são os identificadores e os valores são os dados que queremos armazenar (como se fossem variáveis)
Quando um dicionário tem mais de um item, cada item é separado por vírgula, e o último item não tem vírgula (tem que ser assim, senão dá erro)
'''

# Exibição de um dicionário
print(meus_dados)

# Exibição do tipo do dicionário - saída: dict
print(type(meus_dados))

# OU - outra forma de criar um dicionário em uma única linha

# Criação do dicionário em uma única linha
persona = dict(nome="Maria", sexo="Feminino", idade=28, casado=True)

# Exibição do dicionário e do tipo dele
print(persona)
print(type(persona))

# Exibição mais detalhada
print(f"O nome é: {persona["nome"]}, do sexo: {persona["sexo"]}")

# DICIONÁRIO VAZIO

# Declaração de um dicionário vazio
dict1 = {}

# Exibição dele
print(dict1)

# ADICIONANDO UM DADO AO DICIONÁRIO VAZIO!!
dict1["chave1"] = "Não está mais vazio!!"

# Exibição do novo dicionário
print(dict1)

# LISTA JUNTO COM DICIONÁRIOS

# Criação do dicionário com a lista
dict2 = {
    "Pessoa01": ["william", 30, "Professor"],
    "Pessoa02": ["Julia", 50, "Médica"]
}

'''
ESTRUTURA:

nomeDicionario = {
    "chave1": [valor1, valor2, valor3],
    "chave2": [valor1, valor2, valor3]
}

Ou seja, podemos armazenar listas dentro de um dicionário
Isso pode ser útil para armazenar informações de uma pessoa, por exemplo
'''

# Exibição do dicionário e de seu tipo
print(dict2)
print(type(dict2))

# ACESSANDO ELEMENTOS DE UM DICIONÁRIO
print(dict2["Pessoa02"][0])

'''
ESTRUTURA DO ACESSO:

nomeDicionario["chave"][índice]

OU

nomeDicionario["chave"]["chaveInterna"]

OU

nomeDicionario["chave"][índice]["chaveInterna"]

OU

nomeDicionario["chave"]["chaveInterna"][índice]

EXEMPLOS:

dict2["Pessoa02"][0] - acessa o nome da Pessoa02
dict2["Pessoa02"][1] - acessa a idade da Pessoa02

dict2["Pessoa02"]["Médica"] - acessa a profissão da Pessoa02

MAIS COMPLEXO

dict2["Pessoa02"][0]["Médica"] - acessa a profissão da Pessoa02
'''

# DICIONÁRIO DENTRO DE UM DICIONÁRIO

pessoa = {
    "nome": "Samuel",
    "idade": 16,
    "enderco": {
        "rua": "Tal",
        "cidade": "Tal Tal",
        "estado": "Tal Tal Tal"
    }
}

'''
ESTRUTURA:

nomeDicionario = {
    "chave1": "valor1",
    "chave2": "valor2",
    "chave3": {
        "chaveInterna1": "valorInterno1",
        "chaveInterna2": "valorInterno2"
    }
}

OU

nomeDicionario = {
    "chave1": "valor1",
    "chave2": {
        "chaveInterna1": "valorInterno1",
        "chaveInterna2": "valorInterno2"
    },
    "chave3": "valor3"
}

OU

nomeDicionario = {
    "chave1": {
        "chaveInterna1": "valorInterno1",
        "chaveInterna2": "valorInterno2"
    },
    "chave2": "valor2",
    "chave3": "valor3"
}

EXPLICAÇÃO DA ESTRUTURA:

Podemos armazenar um dicionário dentro de outro dicionário, isso é útil para armazenar informações mais detalhadas de uma pessoa, por exemplo
'''

# Exibição
print(pessoa)

# Acessando dados
print("Idade:", pessoa["idade"])
print("Endereço", pessoa["enderco"]["rua"], pessoa["enderco"]["cidade"])

'''
ESTRUTURA DO ACESSO:

nomeDicionario["chaveInterna"]["chaveInternaInterna"]

OU

nomeDicionario["chaveInterna"]["chaveInternaInterna"]["chaveInternaInternaInterna"]

EXEMPLOS:

pessoa["idade"] - acessa a idade da pessoa
pessoa["enderco"]["rua"] - acessa a rua do endereço da pessoa
pessoa["enderco"]["cidade"] - acessa a cidade do endereço da pessoa
'''

# ALTERANDO DADOS DE UM DICIONÁRIO
pessoa["idade"] = 17
pessoa["enderco"]["rua"] = "Rua Tal Tal"

# Exibição do dicionário e de seu tipo
print(pessoa)
print(type(pessoa))

# ARMAZENAR LISTAS DENTRO DE UM DICIONÁRIO

# Criação do dicionário
dict3 = {
    "lista1": [1, 2, 3, 4, 5],
    "lista2": [6, 7, 8, 9, 10]
}

# ADICIONANDO LISTAS AO DICIONÁRIO
dict3["lista3"] = [11, 12, 13, 14, 15]

# Exibição
print(dict3)