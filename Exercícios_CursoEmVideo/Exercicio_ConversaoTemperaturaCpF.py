# Crie um algoritmo para converter celsius para fahrenheit
# para realisar este exercício precisei buscar a Fórmula (0 °C × 9/5) + 32 = 32 °F

Celsius = float(input("Digite a temperatura em celsius: "))
print("A temperatura digitada foi {} graus celsius".format(Celsius))
print("Temperatura comvertida para graus fahrenheit é de {:.2f} graus fahrenheit".format((Celsius*9/5)+32))

# a gora ao contrário vamos fazer de fahrenheit para celsius

Fahrenheit = float(input("Digite a temperatura em fahrenheit: "))
print("Temperatura em celsius é de: {:.2f}".format((Fahrenheit-32)*5/9))

# Fórmula simples Celsius para Fahrenheit 9 * C / 5 + 32