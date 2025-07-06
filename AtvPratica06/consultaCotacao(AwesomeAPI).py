import requests

def consultar_cotacao(moeda: str):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave in dados:
            cotacao = dados[chave]
            print("=== Cotação Atual ===")
            print(f"Moeda: {cotacao['name']}")
            print(f"Valor atual: R$ {cotacao['bid']}")
            print(f"Valor máximo: R$ {cotacao['high']}")
            print(f"Valor mínimo: R$ {cotacao['low']}")
            print(f"Última atualização: {cotacao['create_date']}")
        else:
            print("Moeda não encontrada.")
    else:
        print("Erro ao consultar a cotação.")

# Exemplo de uso
# moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
# consultar_cotacao(moeda)
