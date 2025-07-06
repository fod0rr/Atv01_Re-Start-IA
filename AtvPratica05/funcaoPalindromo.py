def verificar_palindromo(texto: str) -> str:
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"

# Exemplo de uso:
# palavra = input("Digite uma palavra ou frase: ")
# print(f"É palíndromo? {verificar_palindromo(palavra)}")
