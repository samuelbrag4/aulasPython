frase = "Segunda é Tristeza!"

# Aqui o Lower() transforma todas as letras em minúsculas
frase = frase.lower()
print(frase)

# Aqui o Replace() substitui a palavra "Segun" por "Bala". De modo que a primeira palavra tem que ser exatamente igual a palavra que você quer substituir
frase = frase.replace("segun","Bala")
print(frase)

# Aqui o Replace() substitui a palavra "tristeza" por "top". De modo que a primeira palavra tem que ser exatamente igual a palavra que você quer substituir
frase = frase.replace("tristeza","top")
print(frase)

# Em uma única linha

print(frase.lower().replace("segun","Bala").replace("tristeza","top"))
print(frase)
