pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").lower()
    
    if entrada == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Par")
            pares += 1
        else:
            print("Ímpar")
            impares += 1
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números inteiros.")

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
