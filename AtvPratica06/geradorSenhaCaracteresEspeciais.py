import random
import string

def gerar_senha(tamanho: int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso
try:
    tamanho = int(input("Digite a quantidade de caracteres da senha: "))
    print(f"Senha gerada: {gerar_senha(tamanho)}")
except ValueError:
    print("Erro: Digite um número válido.")
