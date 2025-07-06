import requests

def gerar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']

        print("=== Perfil Gerado ===")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao acessar a API.")

# Exemplo de uso
# gerar_usuario_aleatorio()
