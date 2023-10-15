# -- Converta binário em decimal --

# Fabio Oliveira da Silva (42370280)
# Leonardo Silva Moreno Ruiz (32389892)
# Luciano Paranhos (42324882)
# Patrick Rocha de Andrade (42281091)

numero_binario = input("Entre com o número binário: ")
decimal = 0
potencia = 0

numero_binario_range = len(numero_binario) - 1


for i in range(numero_binario_range, -1, -1):
    digito = int(numero_binario[i])
    decimal = decimal + digito * (2 ** potencia)
    potencia = potencia + 1

print(f"O decimal é: {decimal}")
