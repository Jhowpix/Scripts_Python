while True:
    numero = int(input("Digite um numero inteiro: "))
    print('''Escolha uma base para conversão.
    [ 1 ] Converter para BINÁRIO
    [ 2 ] Converter para OCTAL
    [ 3 ] Converter para HEXADECIMAL''')
    numeroEscolhido = int(input("Digite Aqui sua opção: "))
    if numeroEscolhido == 1:
        print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
    elif numeroEscolhido == 2:
        print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
    elif numeroEscolhido == 3:
        print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
    break


