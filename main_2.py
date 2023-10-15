# -- Algoritmo para conversão de número binário para decimal --

# Fabio Oliveira da Silva (42370280)
# Leonardo Silva Moreno Ruiz (32389892)
# Luciano Paranhos (42324882)
# Patrick Rocha de Andrade (42281091)

# Função que converte um número binário para decimal
# Parâmetros:
#   numero_binario: número binário que será convertido
# Retorno:
#   número decimal correspondente ao número binário
def binario_para_decimal(numero_binario):
    # Inicializa as variáveis com 0
    decimal = 0
    potencia = 0

    # O comando reversed inverte a ordem do número binário digitado
    # Exemplo: reversed("100") -> "001"
    for digito in reversed(numero_binario):
        decimal = decimal + int(digito) * (2 ** potencia)
        potencia = potencia + 1
    return decimal

# Solicita ao usuário um número binário
# O número binário precisa ser tratado como string para que o comando reversed
# funcione corretamente.
numero_binario = input("Entre com o número binário: ")

# Imprime o número decimal correspondente
print(f"O decimal é: {binario_para_decimal(numero_binario)}")
