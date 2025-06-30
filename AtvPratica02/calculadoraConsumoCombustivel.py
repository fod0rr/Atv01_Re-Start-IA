# -*- coding: utf-8 -*-

"""
Este programa calcula o consumo médio de combustível de um veículo.
"""

# Dados de entrada
distancia_percorrida = 300  # em km
combustivel_gasto = 25     # em litros

# Cálculo do consumo médio
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibição dos resultados
print("--- Calculadora de Consumo de Combustível ---")
print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litros")
print("-" * 45)
print(f"Consumo Médio: {consumo_medio:.2f} km/l")

"""--- Calculadora de Consumo de Combustível ---
Distância Percorrida: 300 km
Combustível Gasto: 25 litros
---------------------------------------------
Consumo Médio: 12.00 km/l"""