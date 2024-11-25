# Escreva um programa em Python para obter valores exclusivos de uma lista. (set)

# Exemplo de lista com valores duplicados
lista = [10, 20, 30, 40, 20, 50, 60, 40]

# Convertendo a lista para um set para obter valores exclusivos
valores_unicos = set(lista)

# Convertendo de volta para lista, se necessário
valores_unicos_lista = sorted(list(valores_unicos))

# Exibindo os valores exclusivos
print(f"Os valores únicos da lista são: \n{valores_unicos_lista} \nEles estão em ordem crescente!")

'''
EXPLICAÇÃO:

O "set()" serve para criar um conjunto em Python, que é uma coleção não ordenada de elementos únicos. 
Ao converter uma lista para um set, todas as duplicatas são removidas automaticamente. 
Isso é útil quando queremos obter apenas os valores exclusivos de uma lista.

O "sorted()" serve para deixar os valores de uma lista em ordem crescente (ou de acorodo com algum parâmetro que for passado).
Ao converter a lista com o sorted, os valores são organizados em ordem crescente.
Muito útil para manter sempre a organização 
'''