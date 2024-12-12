import pandas as pd
import glob
import os

# Caminho para onde os arquivos do exel estão salvos
caminho = 'C:/Users/Aluno/Desktop/cursoPython/semana/'
arquivos = glob.glob(os.path.join(caminho, "*.xlsx"))

# Lista para armazenar os DataFrames individuais
consolidado = []

# Loop pelos arquivos para combinar
for arquivo in arquivos:
    # Carregar o arquivo do Exel
    df = pd.read_excel(arquivo)
    
    # Extrair o nome do arquivo para identificar a semana
    nome_arquivo = os.path.basename(arquivo).split('.')[0]
    df['Semana'] = nome_arquivo # Adicona uma coluna com a identificação da semana
    
    # Adicionar o DataFrame a lista
    consolidado.append(df)
    
# Combinar todos os DataFrames em um único
df_completo = pd.concat(consolidado, ignore_index=True)

# Salvar o resultado consolidado em um único Exel
df_completo.to_excel('C:/Users/Aluno/Desktop/cursoPython/semana/relatorio_mensal.xlsx', index=False)

print('Planilhas combinadas com sucesso!')