# 1) Código que conta quantos números pares existem em uma lista
def contar_pares(lista):
    return len([num for num in lista if num % 2 == 0])

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Números pares na lista: {contar_pares(lista_numeros)}")

# 2) Código que calcula a média de um dicionário que contém nomes de alunos e suas respectivas notas
def calcular_media(notas_alunos):
    total_notas = sum(notas_alunos.values())
    quantidade_alunos = len(notas_alunos)
    return total_notas / quantidade_alunos

notas_alunos = {"João": 8.5, "Maria": 7.2, "Pedro": 9.0}
print(f"Média das notas dos alunos: {calcular_media(notas_alunos)}")

# 3) Código que retorna uma lista de nomes das pessoas que têm idade superior a 30 anos
def pessoas_acima_de_30(pessoas):
    return [nome for nome, idade in pessoas.items() if idade > 30]

pessoas = {"João": 28, "Maria": 35, "Pedro": 40, "Ana": 25}
print(f"Pessoas com idade superior a 30 anos: {pessoas_acima_de_30(pessoas)}")