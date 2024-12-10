# Leitura de arquivos
with open('atividades/manipulacaoArquivos/samuelPython.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# O bloco with garante que o arquivo seja fechado corretamente após a execução do bloco de código.

# Gravação de arquivos
with open('novo_arquivo.txt', 'w') as arquivo:
    arquivo.write('Este é um novo arquivo criado com Python!\n')
    arquivo.write('Python é uma linguagem de programação muito poderosa!\n')
    arquivo.write('Estou aprendendo a programar em Python!\n')

# Renomear arquivo
import os
os.rename('novo_arquivo.txt', 'novo_arquivo_renomeado.txt')
print('Novo arquivo renomeado com sucesso!')

# Leitura do arquivo renomeado
with open('novo_arquivo_renomeado.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
# Remover arquivo
if os.path.exists('novo_arquivo_renomeado.txt'):
  os.remove('novo_arquivo_renomeado.txt')
  print('Arquivo removido com sucesso!')
else:
  print('Arquivo não encontrado!')