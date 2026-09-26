'''
Exercício Python 54: Crie um programa que leia o
ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.
'''

from datetime import date

atual = date.today().year

totalMaior = 0
totalMenor = 0

for pess in range (1,8):
    nasc = int(input('{} Em que anoa  pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    if idade >= 18:
       totalMaior += 1
    else:
        totalMenor += 1
print('Ao todo tivemos {} pessoas maiores de 18 anos.'.format(totalMaior))
print('Ao todo tivemos {} pessoas menores de 18 anos.'.format(totalMenor))