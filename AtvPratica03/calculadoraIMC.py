# -*- coding: utf-8 -*-

"""
Calcula o Índice de Massa Corporal (IMC) e fornece a classificação.
Fórmula: IMC = peso / (altura * altura)
"""

try:
    # Entrada de peso e altura
    peso = float(input("Digite seu peso em kg (ex: 70.5): "))
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    # Cálculo do IMC
    imc = peso / (altura ** 2)

    # Classificação do IMC
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    # Exibição dos resultados
    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

except ValueError:
    print("Erro: Por favor, digite valores numéricos válidos para peso e altura.")
except ZeroDivisionError:
    print("Erro: A altura não pode ser zero.")
    
"""Digite seu peso em kg (ex: 70.5): 85
Digite sua altura em metros (ex: 1.75): 1.78
Seu IMC é: 26.83
Classificação: Sobrepeso"""