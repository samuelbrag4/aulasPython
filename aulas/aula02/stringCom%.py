nome = "Samuel"

idade = 16

print("olá, %s! Você tem %d anos." % (nome, idade))

# Formatação de string com %s para strings e %d para inteiros
print("olá, %s! Você tem %d anos." % (nome, idade))

# Formatação de string com %f para floats
altura = 1.75
print("Sua altura é %.2f metros." % altura)

# Formatação de string com %x para números hexadecimais
numero = 255
print("O número %d em hexadecimal é %x." % (numero, numero))

# Formatação de string com %o para números octais
print("O número %d em octal é %o." % (numero, numero))

# Formatação de string com %e para notação científica
grande_numero = 123456789
print("O número %d em notação científica é %e." % (grande_numero, grande_numero))

# Formatação de string com %% para incluir um símbolo de porcentagem
print("A porcentagem de conclusão é %d%%." % 75)