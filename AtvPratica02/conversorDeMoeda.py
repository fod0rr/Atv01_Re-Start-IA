# -*- coding: utf-8 -*-

"""
Este programa converte um valor em reais para dólares e euros.
"""

# Dados de entrada
valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Cálculo da conversão
valor_em_dolares = valor_em_reais / taxa_dolar
valor_em_euros = valor_em_reais / taxa_euro

# Exibição dos resultados
print("--- Conversor de Moeda ---")
print(f"Valor em Reais: R$ {valor_em_reais:.2f}")
print(f"Taxa do Dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa do Euro: R$ {taxa_euro:.2f}")
print("-" * 28)
print(f"Valor em Dólares: US$ {valor_em_dolares:.2f}")
print(f"Valor em Euros: € {valor_em_euros:.2f}")

"""--- Conversor de Moeda ---
Valor em Reais: R$ 100.00
Taxa do Dólar: R$ 5.20
Taxa do Euro: R$ 6.15
----------------------------
Valor em Dólares: US$ 19.23
Valor em Euros: € 16.26"""