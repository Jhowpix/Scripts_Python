'''
Faça um programa que calcule a soma entre todos os números
que são múltiplos de três e que se encontram no
intervalo de 1 até 500.
'''

for cont in range(1, 501, 2):
    if cont % 3 == 0:
        print(cont)
