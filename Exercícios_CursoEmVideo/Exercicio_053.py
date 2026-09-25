'''
Exercício Python 53: Crie um programa que leia
uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
'''

palavra = str(input('Digite uma frase: ')).strip().upper()
palavras = palavra.split()
junto = ''.join(palavras)
invertido = ''
for letra in range(len(junto)-1, -1, -1):
    invertido += junto[letra]
if invertido == junto[letra]:
    print('Palavra {}'.format(junto),'não é um palindromo.')
else:
    print('Palavra {}'.format(junto),' é um palindromo.')

#print(junto, invertido)
#print('{}'.format(palavra))