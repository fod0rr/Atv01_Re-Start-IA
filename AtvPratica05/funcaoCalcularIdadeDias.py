from datetime import datetime

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365  # Aproximação simples, sem considerar anos bissextos

# Exemplo de uso:
# nascimento = int(input("Digite o ano de nascimento: "))
# print(f"Idade aproximada em dias: {calcular_idade_em_dias(nascimento)} dias")
