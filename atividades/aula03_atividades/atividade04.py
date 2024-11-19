# String
frase = " Python é uma linguagem de programação poderosa. "

# 1. Remova os espaços em branco no início e no final da string.
frase = frase.strip()
# Exibição
print(f"String sem espaços em branco no início e no final: {frase}")

# 2. Converta toda a string para minúsculas.
frase = frase.lower()
# Exibição
print(f"String em minúsculas: {frase}")

# 3. Substitua a palavra "poderosa" por "versátil".
frase = frase.replace("poderosa", "versátil")
# Exibição
print(f"String com a palavra 'poderosa' substituída por 'versátil': {frase}")