# Crie um algoritmo que escolha de 0 a 5
# e deixe o usurio tentar acertar
from random import randint
from time import sleep
numeroRandom = randint(0, 5)
numeroEscolhido = int(input("O algoritmo criado randomizara um número de 0 a 5 tente acertar qual é: ")))
print("PROCESSANDO...")
sleep(2)
print("PROCESSANDO...")
if numeroRandom == numeroEscolhido:
    print("Você acertou o número escolhido foi: {}".format(numeroRandom))
else:
    print("Não acertou o número escolhido foi: {}".format(numeroRandom))


