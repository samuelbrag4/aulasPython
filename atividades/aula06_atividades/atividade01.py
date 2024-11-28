'''
1) Implemente um código em Python que recebe as notas de um aluno em três disciplinas e armazena essas notas em uma tupla. 
Em seguida, calcule e imprima a média das notas.
'''

# Solicitação de inserção das notas:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Tupla que armazena as notas:
notas = (nota1, nota2, nota3)

# Cálculo da média:
media = sum(notas) / len(notas)

# Impressão dos resultados:
print(f"Olá! As notas inseridas foram: {notas} \n A média das notas é: {media}")

'''
2) Solicita ao usuário que insira o login e a senha,crie uma tupla (usuario(login,senha))
com login e senha e exibe as informações armazenadas. Na última linha tente alterar
usuario[1] = '123645', Qual é o resultado esperado e por que?
'''

# Solicitação de inserção do login e senha:
login = input("Digite o login: ")
senha = input("Digite a senha: ")

# Criação da tupla:
usuario = (login, senha)

# Exibição da tupla:
print(f"O usuário inserido foi: {usuario}")

# Transformando a tupla em lista para alterar a senha:
usuario = list(usuario)

# Alteração da senha:
usuario[1] = '123456'

# Transformando a lista em tupla novamente:
usuario = tuple(usuario)

# Exibição da tupla:
print(f"O usuário inserido com a senha atualizada é: {usuario}")