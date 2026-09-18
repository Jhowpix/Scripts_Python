'''
Faça um programa que calcule a soma entre todos os números
que são múltiplos de três e que se encontram no
intervalo de 1 até 500.
'''

conta = 0
total = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        conta += cont
        total += 1
print('A soma dos números divisíveis por 3 entre 1 e 500 é de {} e a quantidade de valores somados foram de {}'.format(total, conta))
