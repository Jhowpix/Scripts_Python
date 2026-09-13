numero1 = input("Informe o primeiro valor a ser somado: ")
if numero1.isnumeric() == False:
    print("Caracteres inválidos")
else:
    numero1 = int(numero1)
numero2 = input("Informe o segundo valor a ser somado: ")
if numero2.isnumeric() == False:
    print("Caracteres inválidos")
else:
    numero2 = int(numero2)
print("Valores a serem somados: ", numero1, " + ", numero2)
print("A soma entre os dois valores é de: ", numero1  +  numero2)
