import requests

def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print("=== Endereço ===")
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
    else:
        print("Erro ao consultar o CEP.")

# Exemplo de uso
# cep = input("Digite o CEP (somente números): ")
# consultar_cep(cep)
