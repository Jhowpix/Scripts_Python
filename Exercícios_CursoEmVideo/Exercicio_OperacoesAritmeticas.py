# Operações Aritméticas
# + - * / ** // %
# = sinal de atribuição
# == sinal de igual

# operando e operador
#    10         +        1  == 11

# Crie um prigrama onde voce leia um número
# e mostre seu antecessor e seu sucessor

numeroAntecessorSucessor = int(input("Digite um número para saber seu antecessor e seu sucessor "))
print("O número digitado foi {} seu número antecessor é {} e seu número sucessor é {} ".format(numeroAntecessorSucessor, numeroAntecessorSucessor-1, numeroAntecessorSucessor+1))
# no caso a cima foi criada somente uma variavel (numeroAntecessorSucessor) e usado operação direto no valor da variavel

numeroMultiplicacaoRaiz = int(input("Digite um valor para saber seu dobro seu triplo e sua raiz quadrada "))
print("O número digitado foi {} seu dobro é {} seu triplo é {} sua raiz é {}".format(numeroMultiplicacaoRaiz, numeroMultiplicacaoRaiz*2, numeroMultiplicacaoRaiz*3, numeroMultiplicacaoRaiz**(1/2)))
# pode ser usado pow exemplo pow(numeroMultiplicacaoRaiz, (1/2)) com está formula tambem conseguimos
# obter a raiz quadrada de um número

#media com formatação apos a virgula
n1 = float(input("Digite a nota da prova do aluno: "))
n2 = float(input("Digite a nota do trabalho do aluno: "))
media = (n1+n2)/2
print("A média do aluno é {:.1f}".format(media))
# Repare como formatar as casas após a virgula :.1f
#                                após a virgula ter somente 1 casa
# para deixar mais claro :.2f após a virgula ter somente 2 casa

