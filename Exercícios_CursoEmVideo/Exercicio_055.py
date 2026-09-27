'''
Exercício Python 55: Faça um
programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

pesoMaior = 0
pesoMenor = 0

for c in range(1, 6):
    peso = int(input('{} Digite o seu peso: '.format(c)))

    if peso == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso

print('O maior peso é de {}'.format(pesoMaior))
print('O menor peso é de {}'.format(pesoMenor))

# Existe um bug neste script se digitar valores do menor para o maior ]
# o resultado do menor sera sempre zero