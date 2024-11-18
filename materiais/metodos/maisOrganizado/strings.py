# Método ascii()
# Retorna uma versão legível de um objeto, mas substitui caracteres não ASCII por escapes.
# Exemplo:
texto = 'Pythön'
print(ascii(texto))  # Saída: 'Pyth\xf6n'

# Método format()
# Formata uma string usando substituições de campo.
# Exemplo:
print("Hello, {}!".format("world"))  # Saída: Hello, world!

# Método join()
# Junta uma sequência de strings com um delimitador.
# Exemplo:
sequencia = ['a', 'b', 'c']
print('-'.join(sequencia))  # Saída: a-b-c

# Método lower()
# Converte todos os caracteres de uma string para minúsculas.
# Exemplo:
texto = "HELLO"
print(texto.lower())  # Saída: hello

# Método upper()
# Converte todos os caracteres de uma string para maiúsculas.
# Exemplo:
texto = "hello"
print(texto.upper())  # Saída: HELLO