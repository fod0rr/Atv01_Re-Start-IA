# -*- coding: utf-8 -*-

"""
Calcula a média ponderada de um aluno e determina sua situação.
Pesos: N1(2), N2(3), N3(4), N4(1).
"""
try:
    # Leitura das quatro notas
    notas_str = input("Digite as quatro notas do aluno separadas por espaço (ex: 2.0 4.0 7.5 8.0): ").split()
    n1, n2, n3, n4 = map(float, notas_str)

    # Cálculo da média ponderada
    media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)

    # Exibe a média inicial
    print(f"Media: {media:.1f}")

    # Verifica a situação do aluno
    if media >= 7.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")
    else:  # Média entre 5.0 e 6.9
        print("Aluno em exame.")
        
        # Leitura da nota do exame
        nota_exame = float(input("Digite a nota do exame: "))
        print(f"Nota do exame: {nota_exame:.1f}")

        # Recálculo da média
        media_final = (media + nota_exame) / 2

        # Verifica a situação final
        if media_final >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        
        # Exibe a média final
        print(f"Media final: {media_final:.1f}")

except (ValueError, IndexError):
    print("Entrada inválida. Certifique-se de digitar quatro números separados por espaço.")
    
"""Digite as quatro notas do aluno separadas por espaço (ex: 2.0 4.0 7.5 8.0): 2.0 6.5 4.0 9.0
Media: 5.4
Aluno em exame.
Digite a nota do exame: 6.4
Nota do exame: 6.4
Aluno aprovado.
Media final: 5.9"""