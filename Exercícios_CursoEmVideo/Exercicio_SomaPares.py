'''
Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o
valor digitado for ímpar, desconsidere-o.
'''

soma = 0
total = 0

for x in range(1, 7):
    n = int(input('Digite seis digito para serem calculados: '))
    if n % 2 == 0:
        soma += n
        total += 1
print('A soma entre todos os números pares digitados foi {}'.format(soma))

