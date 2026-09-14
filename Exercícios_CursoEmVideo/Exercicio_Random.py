# crie um algoritmo que sorteie um nome
import random

nome1 = str(input("Digite o nome do primeiro aluno: "))
nome2 = str(input("Digite o nome do segundo aluno: "))
nome3 = str(input("Digite o nome do terceiro aluno: "))
nome4 = str(input("Digite o nome do quarto aluno: "))
lista = [nome1, nome2, nome3, nome4]
escolha = random.choice(lista)
print("O nome sorteado foi ",escolha)

# Lista de alunos, de uma ordem aleatória para uma lista
nome1 = str(input("Digite o nome do primeiro aluno: "))
nome2 = str(input("Digite o nome do segundo aluno: "))
nome3 = str(input("Digite o nome do terceiro aluno: "))
nome4 = str(input("Digite o nome do quarto aluno: "))

listaDeOrdem = [nome1, nome2, nome3, nome4]
random.shuffle(listaDeOrdem)
print("Sequência sorteada foi {}".format(listaDeOrdem))