# Usando o bloco with para garantir que o arquivo seja fechado corretamente
with open('atividades/manipulacaoArquivos/samuelPython.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
# O bloco with garante que o arquivo seja fechado corretamente após a execução do bloco de código.