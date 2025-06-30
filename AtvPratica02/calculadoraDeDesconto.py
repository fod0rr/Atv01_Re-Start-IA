# -*- coding: utf-8 -*-

"""
Este programa calcula o desconto em uma loja e o preço final de um produto.
"""

# Dados de entrada
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Cálculo do desconto e do preço final
valor_desconto = (porcentagem_desconto / 100) * preco_original
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print("--- Calculadora de Desconto ---")
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print("-" * 31)
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")

"""--- Calculadora de Desconto ---
Produto: Camiseta
Preço Original: R$ 50.00
Desconto: 20%
-------------------------------
Valor do Desconto: R$ 10.00
Preço Final: R$ 40.00"""