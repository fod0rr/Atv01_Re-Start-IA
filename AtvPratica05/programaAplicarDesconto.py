try:
    preco_original = float(input("Digite o preço original do produto: "))
    percentual_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
    
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto

    print(f"Preço final com desconto: R${preco_final:.2f}")
except ValueError:
    print("Erro: Entrada inválida. Digite números válidos para o preço e desconto.")
