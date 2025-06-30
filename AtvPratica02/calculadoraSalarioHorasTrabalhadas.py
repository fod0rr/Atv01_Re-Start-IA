# -*- coding: utf-8 -*-

"""
Este programa lê os dados de um funcionário, calcula seu salário
e exibe o número do funcionário e o salário calculado.
"""

# Entrada de dados pelo usuário
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Exibição da saída formatada
print(f"\nNÚMERO = {numero_funcionario}")
print(f"SALÁRIO = R$ {salario:.2f}")

"""Digite o número do funcionário: 25
Digite a quantidade de horas trabalhadas: 100
Digite o valor recebido por hora: 5.50

NÚMERO = 25
SALÁRIO = R$ 550.00"""