'''
Crie um arquivo chamado dados.txt que contenha alguns dados ficticios 
Em seguida, escreva um programa que leia este arquivo e exiba ele na tela
'''

# Criação do arquivo dados.txt
arquivo = open('dados.txt', 'w')
arquivo.write('Nome: João\n')
arquivo.write('Idade: 25\n')
arquivo.write('Sexo: Masculino\n')
arquivo.write('Profissão: Programador\n')
arquivo.write('Salário: 5000\n')

# Leitura do arquivo dados.txt
arquivo = open('dados.txt', 'r')
print(arquivo.read())
arquivo.close()
