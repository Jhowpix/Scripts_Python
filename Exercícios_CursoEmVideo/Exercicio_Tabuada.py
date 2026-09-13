# Crie um program que pegue um numero inteiro
# e crie uma tabuada completa
numeroTabuada = int(input("Digite um numero para a tabuada: "))
for i in range(11):
    numero = numeroTabuada * i
    print(numeroTabuada, " x ", numero, " = ", numeroTabuada)