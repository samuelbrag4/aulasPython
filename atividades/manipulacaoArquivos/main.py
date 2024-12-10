# Usando o bloco with para garantir que o arquivo seja fechado corretamente
with open('atividades/manipulacaoArquivos/samuelPython.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
# O bloco with garante que o arquivo seja fechado corretamente após a execução do bloco de código.

# Gravação de arquivos

with open('novo_arquivo.txt', 'w') as arquivo:
    arquivo.write('Este é um novo arquivo criado com Python!\n')
    arquivo.write('Python é uma linguagem de programação muito poderosa!\n')
    arquivo.write('Estou aprendendo a programar em Python!\n')