# -*- coding: utf-8 -*-

"""
Solicita a idade do usuário e o classifica em:
Criança (0-12), Adolescente (13-17), Adulto (18-59), Idoso (60+).
"""

# Entrada da idade
try:
    idade = int(input("Digite sua idade: "))

    # Verificação e classificação usando if-elif-else
    if 0 <= idade <= 12:
        classificacao = "Criança"
    elif 13 <= idade <= 17:
        classificacao = "Adolescente"
    elif 18 <= idade <= 59:
        classificacao = "Adulto"
    elif idade >= 60:
        classificacao = "Idoso"
    else:
        # Caso a idade seja um número negativo
        classificacao = "Idade inválida."

    # Exibição do resultado
    print(f"Classificação: {classificacao}")

except ValueError:
    print("Por favor, digite um número inteiro válido para a idade.")
    
"""Digite sua idade: 25
Classificação: Adulto

Digite sua idade: 10
Classificação: Criança"""