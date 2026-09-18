'''
Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0, com
uma pausa de 1 segundo entre eles.
'''
print('-'*30)
print('CONTAGEM REGRESSIVA')
print('-'*30)
import time
for c in range(1, 11):
    c = c - 1
    d = 10 - c
    time.sleep(1)
    print(d)

'''
Solução do Professor Gustavo Guanabara 

for cont in range(10, -1, -1):
    time.sleep(1)
    print(cont)
'''