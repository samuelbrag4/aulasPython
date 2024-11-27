# TUPLA - é uma coleção de elementos ordenada e imutável (semelhante a lista).

'''
ESTRUTURA:

nomeTupla = (elemento1, elemento2, elemento3, ..., elementoN)

EXEMPLO:
tupla = (1, 2, 3, 4, ..., n)

CARACTERÍSTICAS:

- Tuplas são imutáveis, ou seja, não podem ser alteradas após a sua criação.
- Tuplas são ordenadas, ou seja, os elementos possuem uma ordem definida.
- Tuplas permitem elementos duplicados.
- Tuplas são definidas por parênteses ().
- Podem armazenar todos os tipos de dados.
'''

# CRIANDO UMA TUPLA
tupla = (1, 2, 3, 4, 5)

# OU - com tipos de dados diferentes
tuplaDadosDiferentes = (1, 'Python', 3.14, True)

# ACESSANDO ELEMENTOS DE UMA TUPLA
print(tupla[0]) # Saída: 1
print(tupla[-1]) # Saída: 5

'''
EXPLICAÇÃO DE ACESSO:

- O acesso aos elementos de uma tupla é feito através de um índice.
- O índice de uma tupla começa em 0.

EXEMPLO:

tupla = (1, 2, 3, 4, 5)

- tupla[0] -> 1

nomeTupla[índice] -> elemento
'''

# EXIBINDO UMA TUPLA E O SEU TIPO
print(tupla, tuplaDadosDiferentes)
print(type(tupla))
print(type(tuplaDadosDiferentes))

# VERIFICAR O TAMANHO DA TUPLA - len()
print(len(tupla)) # Saída: 5

# INSERINDO ELEMENTOS EM UMA TUPLA - não é possível

# tupla = tupla + (6, 7, 8) # Errado!
# Não é certo se fazer isso. Porém é uma gambiarra para adicionar elementos em uma tupla.

# OU

#tupla.append(6) # Erro

'''
EXPLICAÇÃO:

- Tuplas são imutáveis, ou seja, não podem ser alteradas após a sua criação.
- Para adicionar elementos em uma tupla, é necessário criar uma nova tupla.
'''

# Exibindo a tupla
print(tupla)

# DELETANDO UM ITEM DE UMA TUPLA - não é possível

# del tupla[0] # Erro

# OU

# tupla = tupla - (1, 2, 3) # Erro

'''
EXPLICAÇÃO:

- Tuplas são imutáveis, ou seja, não podem ser alteradas após a sua criação.
- Para remover elementos de uma tupla, é necessário criar uma nova tupla.
'''

# ALTERANDO CONTEÚDO DE UMA TUPLA - não é possível

# tupla[1] = 20 # Erro

'''
EXPLICAÇÃO:

- Tuplas são imutáveis, ou seja, não podem ser alteradas após a sua criação.
- Para alterar elementos de uma tupla, é necessário criar uma nova tupla.
'''

# CONVERTENDO UMA TUPLA EM LISTA

# Criação da tupla
minhaTupla = (1, 2, 3, 4, 5)

# Converção da tupla para lista
listaResultado = list(minhaTupla)

# Exibição da tupla e de seu tipo
print(minhaTupla)
print(type(minhaTupla))

# Exibição da lista e de seu tipo
print(listaResultado)
print(type(listaResultado))

# CONVERTENDO UMA LISTA EM TUPLA
lista = [1, 2, 3, 4, 5]

# Converção da lista para tupla
tuplaResultado = tuple(lista)

# Exibição da lista e de seu tipo
print(lista)
print(type(lista))

# Exibição da tupla e de seu tipo
print(tuplaResultado)
print(type(tuplaResultado))