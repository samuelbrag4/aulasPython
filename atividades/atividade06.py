# Duas listas de cidades do Norte e Sul do Brasil

# Cidades do Norte
norte = ["Manaus", "Belém", "Palmas", "Porto Velho", "Boa Vista", "Macapá", "Rio Branco"]

# Cidades do Sul
sul = ["Curitiba", "Florianópolis", "Porto Alegre", "Londrina", "Joinville", "Pelotas", "Criciúma"]

# Lista geral
cidades = norte + sul

# Exibições das listas

# Norte
print(f"Cidades do Norte: {norte}")

# Sul
print(f"Cidades do Sul: {sul}")

# Geral
print(f"Cidades Gerais: {cidades}")

print("\n")
print("-----SEPARAÇÃO-----")
print("\n")

# ----------COM EXTEND()

# Cidades do Norte
norte = ["Manaus", "Belém", "Palmas", "Porto Velho", "Boa Vista", "Macapá", "Rio Branco"]

# Cidades do Sul
sul = ["Curitiba", "Florianópolis", "Porto Alegre", "Londrina", "Joinville", "Pelotas", "Criciúma"]

# Lista geral
cidades.extend(norte)
cidades.extend(sul)

# Exibições das listas
print(f"Cidades do Norte: {norte}")
print(f"Cidades do Sul: {sul}")
print(f"Cidades Gerais: {cidades}")

# -----OU-----

print("\n")
print("-----SEPARAÇÃO-----")
print("\n")

# Lista geral
cidades.extend(["Manaus", "Belém", "Palmas", "Porto Velho", "Boa Vista", "Macapá", "Rio Branco"])
cidades.extend(["Curitiba", "Florianópolis", "Porto Alegre", "Londrina", "Joinville", "Pelotas", "Criciúma"])

# Exibições das listas
print(f"Cidades do Norte: {norte}")
print(f"Cidades do Sul: {sul}")
print(f"Cidades Gerais: {cidades}")