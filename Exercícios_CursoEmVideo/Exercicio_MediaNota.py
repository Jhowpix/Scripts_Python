# Crie um programa que leia a nota
# de um trabalho e a nota de uma prova
# e de a media dos dois e
# mostre para o usuario
notaProva = int(input("Digite a nota da prova do aluno: "))
notaTrabalho = int(input("Digite a nota do trabalho do aluno: "))
notaMedia = notaProva * notaTrabalho / 2
print("Nota média do aluno: ", notaMedia)