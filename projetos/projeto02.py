import pandas as pd

# Gerar dados
nomeA1 = input('Digite o nome da célula A1: ')
nomeB1 = input('Digite o nome da célula B1: ')
nomeC1 = input('Digite o nome da célula C1: ')
idadeA2 = int(input('Digite a idade da célula A2: '))
idadeB2 = int(input('Digite a idade da célula B2: '))
idadeC2 = int(input('Digite a idade da célula C2: '))
sexoA3 = input('Digite o sexo da célula A3: ')
sexoB3 = input('Digite o sexo da célula B3: ')
sexoC3 = input('Digite o sexo da célula C3: ')

# Armazenar dados
df = pd.DataFrame({
    'Nome': [nomeA1, idadeA2, sexoA3],
    'Idade': [nomeB1, idadeB2, sexoB3],
    'Sexo': [nomeC1, idadeC2, sexoC3]
})

# Criação de uma nova coluna na planilha utilizando input para que o usuário insira os valores

# Solicitações de novos dados
nomeColuna = input('Digite o nome da nova coluna: ')

newColumnD1 = input('Digite o valor D1 da nova coluna: ')
newColumnD2 = input('Digite o valor D2 da nova coluna: ')
newColumnD3 = input('Digite o valor D3 da nova coluna: ')

# Criação da nova coluna
df[nomeColuna] = [newColumnD1, newColumnD2, newColumnD3]

# Verificação de criação da nova coluna
print('Nova coluna criada com sucesso!')

# Criação da planilha
df.to_excel('C:/Users/Aluno/Desktop/cursoPython/exelCursoPython_Input.xlsx', index=False)

# Verificação de criação da planilha
print('Planilha criada com sucesso!')