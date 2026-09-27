'''
Exercício Python 56: Desenvolva um programa
que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos.
'''


somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0

for c in range(1,5):
    print('------- {} Pessoa --------'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaIdade += idade
    if c == 1 and sexo == 'M':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo == 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome

mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {}'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeVelho))

