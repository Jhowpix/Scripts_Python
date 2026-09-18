'''
Refaça o DESAFIO 9, mostrando a tabuada de um número
que o usuário escolher, só que agora
utilizando um laço for
'''

n = int(input('Digite um número para obter a sua tabuada: '))
for cont in range(0, 11):
    print('{} x {} = {}'.format(cont, n, cont*n))