# -*- coding: utf-8 -*-

"""
Converte temperaturas entre Celsius (C), Fahrenheit (F) e Kelvin (K).
"""

def converter_temperatura():
    try:
        # Solicita os dados ao usuário
        valor = float(input("Digite a temperatura: "))
        unidade_origem = input("Qual a unidade de origem? (C, F, K): ").upper()
        unidade_destino = input("Para qual unidade deseja converter? (C, F, K): ").upper()

        # Validação das unidades
        if unidade_origem not in "CFK" or unidade_destino not in "CFK":
            print("Unidades inválidas. Use C, F ou K.")
            return

        # Se as unidades forem iguais, não há conversão a fazer
        if unidade_origem == unidade_destino:
            resultado = valor
        else:
            # 1. Converte a temperatura de origem para Celsius (unidade base)
            temp_celsius = 0
            if unidade_origem == 'C':
                temp_celsius = valor
            elif unidade_origem == 'F':
                temp_celsius = (valor - 32) * 5/9
            elif unidade_origem == 'K':
                temp_celsius = valor - 273.15

            # 2. Converte de Celsius para a unidade de destino
            if unidade_destino == 'C':
                resultado = temp_celsius
            elif unidade_destino == 'F':
                resultado = (temp_celsius * 9/5) + 32
            elif unidade_destino == 'K':
                resultado = temp_celsius + 273.15

        # Exibe o resultado formatado
        print(f"\n{valor:.2f}°{unidade_origem} é igual a {resultado:.2f}°{unidade_destino}")

    except ValueError:
        print("Valor de temperatura inválido. Por favor, insira um número.")

# Executa a função
converter_temperatura()

"""Digite a temperatura: 100
Qual a unidade de origem? (C, F, K): C
Para qual unidade deseja converter? (C, F, K): F

100.00°C é igual a 212.00°F"""