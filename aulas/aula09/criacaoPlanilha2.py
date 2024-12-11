import pandas as pd

# Gerar dados
df = pd.DataFrame({
    'Nome': ['João', 'Maria', 'José', 'Jane'],
    'Idade': [25, 13, 22, 18],
    'Sexo': ['M', 'F', 'M', 'F']
})

# Criando uma nova coluna que utiliza a coluna de idade para verificar se a pessoa é maior de idade
df['Categoria'] = df['Idade'].apply(lambda x: 'Maior de Idade' if x >= 18 else 'Menor de Idade')

# Criação da planilha
df.to_excel('C:/Users/Aluno/Desktop/cursoPython/exelCursoPython_NewColumn.xlsx', index=False)

# Verificação de criação da planilha
print('Planilha criada com sucesso!')