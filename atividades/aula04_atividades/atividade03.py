'''
Dada a seguinte lista em Python: numeros = [1, 3, 5, 7, 9], como você obteria o
resultado da multiplicação de todos os elementos da lista? (Sem usar laço de repetição)
'''

# Lista de números 
numeros = [1, 3, 5, 7, 9]

resultado_tentativa01 = 1

# Loop de for
for num in numeros:
    resultado_tentativa01 *= num

# Exibição do resultado
print(resultado_tentativa01)

# Tentativa 2 sem o For

# Lista de números 
numeros = [1, 3, 5, 7, 9]

# Multiplicação de todos os elementos da lista usando eval
resultado = eval('*'.join(map(str, numeros)))

# Exibição do resultado
print(resultado)

'''
EXPLICAÇÃO:

O método eval() interpreta uma string contendo código Python e executa esse código.
O método join() combina os elementos de uma lista em uma única string, usando um delimitador especificado.
O método map() aplica uma função a todos os itens de uma lista (ou qualquer iterável) e retorna um iterador com os resultados.
'''

'''
Considere a lista: cores = ["vermelho", "azul", "verde", "amarelo", "roxo"].
Como você removeria o segundo elemento da lista sem utilizar a estrutura de controle
if?
'''

# Declaração da variável
cores = ["vermelho", "azul", "verde", "amarelo", "roxo"]

# Remoção do elemento
sem_segundo_elemento = cores.pop(1)

# Exibição do resultado
print(sem_segundo_elemento)

'''
Dada a lista frutas = ["maçã", "banana", "laranja", "morango"], como você
adicionaria a fruta "uva" no final da lista.
'''

# Declaração da lista
frutas = ["maçã", "banana", "laranja", "morango"]

# Adicionando "uva" ao final da lista
frutas.append("uva")

# Exibição da lista atualizada
print(frutas)

'''
Suponha a lista: nomes = ["Alice", "Bob", "Charlie", "David"]. Como você
verificará se "Alice" está na lista sem usar a estrutura if?
'''

# Declaração da lista
nomes = ["Alice", "Bob", "Charlie", "David"]

# Verificação do nome
tem_alice = "Alice" in nomes

# Exibição do valor booleano que indicará se tem o nome ou não
print(tem_alice)