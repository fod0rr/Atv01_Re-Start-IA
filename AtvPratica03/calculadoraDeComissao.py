# -*- coding: utf-8 -*-

"""
Calcula o salário total de um vendedor com comissão de 15%.
"""

try:
    # Entrada de dados
    nome_vendedor = input("Digite o nome do vendedor: ")
    salario_fixo = float(input("Digite o salário fixo: R$ "))
    total_vendas = float(input("Digite o total de vendas no mês: R$ "))

    # Cálculo da comissão (15% de 0.15)
    comissao = total_vendas * 0.15
    salario_total = salario_fixo + comissao

    # Saída formatada
    print(f"\nTOTAL A RECEBER = R$ {salario_total:.2f}")

except ValueError:
    print("Erro: os valores de salário e vendas devem ser numéricos.")
    
"""Digite o nome do vendedor: JOAO
Digite o salário fixo: R$ 500.00
Digite o total de vendas no mês: R$ 1230.30

TOTAL A RECEBER = R$ 684.55"""