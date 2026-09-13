# Crie um programa para mostrar todos os tipos do dado coletado
dadoColetado = input("Digite algo: ")
# O dadoColedo neste script é um objeto
# todos objeto tem metodos 
print("O tipo primitivo deste dados é: {}".format(type(dadoColetado)))
print("Possui estapaço no dado coletado ? {}".format(dadoColetado.isspace()))
print("O dado coletado é número ? {}".format(dadoColetado.isnumeric()))
print("O dado coletado é uma string ? {}".format(dadoColetado.isascii()))
print("O dado coletado é alfabético ? {}".format(dadoColetado.isalpha()))
print("O dado coletado é alfanúmerico ? {}".format(dadoColetado.isalnum()))
print("O dado coletado está com a formatação em maiusculas ? {}".format(dadoColetado.isupper()))
print("O dado coletado está formatado em minusculas ? {}".format(dadoColetado.islower()))
print("O dado coletado está capitalizado ? {}".format(dadoColetado.istitle()))