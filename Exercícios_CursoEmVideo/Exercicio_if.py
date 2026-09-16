# A aula se resume a ensinar a estrutura if elif else
# estrutura condicional

'''

nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
    print("Que nome bonito")
elif nome == 'Haruyoshi':
    print("Que nome diferente")
else:
    print("O nome digitado foi:",nome)
'''

from _pydatetime import date

idadeNacimento = int(input('Digite ano de nascimento: '))
idade = idadeNacimento - 17

anoAtual = date.today().year
anoQueFalta = anoAtual - idade

anosPassados = anoAtual - idadeNacimento - 17
if idade == 17:
    print("Este é seu ano de alistamento")
elif anoAtual <= 16:
    print("Falta {} anos para seu alistamento".format(anoQueFalta))
elif anoAtual > 17:
    print("Ja se passaram {} anos do seu alistamento".format(anosPassados))