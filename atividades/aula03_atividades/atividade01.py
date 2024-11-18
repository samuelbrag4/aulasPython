# Solicitação da inserção do nome do vendedor 
nome_vendedor = input("Olá vendedor! Digite seu nome: ")

# Solicitação da inserção do salário fixo do vendedor
salario_fixo = float(input("Digite o seu salário fixo: R$"))

# Solicitação da inserção do total de vendas do vendedor
total_vendas = float(input("Digite o total de vendas: R$"))

# Calculo da comissão (15% sobre o total de vendas)
comissao = total_vendas * 0.15

# Calculo do total a receber
total_a_receber = salario_fixo + comissao

# Exibição do resultado
print(f"{nome_vendedor}, o total a receber no final do mês é: R${total_a_receber:.2f}")
# O .2f é utilizado para limitar o número de casas decimais a 2