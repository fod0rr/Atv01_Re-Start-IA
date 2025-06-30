# -*- coding: utf-8 -*-

"""
Verifica se um ano é bissexto.
Regras:
1. Divisível por 4.
2. Não pode ser divisível por 100, a menos que...
3. Seja também divisível por 400.
"""

try:
    ano = int(input("Digite um ano para verificar se é bissexto: "))

    # Aplica a lógica do ano bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para o ano.")
    
"""Digite um ano para verificar se é bissexto: 2024
O ano 2024 é bissexto.

Digite um ano para verificar se é bissexto: 1900
O ano 1900 não é bissexto."""