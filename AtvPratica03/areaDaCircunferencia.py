# -*- coding: utf-8 -*-

"""
Calcula a área de uma circunferência.
A fórmula é: área = pi * raio^2
Considerando pi = 3.14159265
"""

# Definição do valor de pi
PI = 3.14159265

# Entrada de dados pelo usuário
# A função float() converte o texto digitado para um número de ponto flutuante.
raio = float(input("Digite o valor do raio: "))

# Cálculo da área
area = PI * (raio ** 2)

# Saída formatada com 4 casas decimais
print(f"A={area:.4f}")

"""Digite o valor do raio: 2.00
A=12.5664

Digite o valor do raio: 100.64
A=31819.3103"""