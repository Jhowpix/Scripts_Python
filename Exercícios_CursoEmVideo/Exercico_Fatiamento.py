# Crie um algoritmo  que leia o nome completo de uma pessoa
# e mostre
# O nome com todas as letras maiúsculas e minúsculas
# Quantas letras ao total sem considerar os espaços
# Quantas letras tem o primeiro nome.

nome = str(input("digite seu nome  "))
print(nome.upper())
print(nome.lower())
# print(nome.title())
# print(nome.capitalize())
# print(nome.strip(" ", ))
print(len(nome), " Quantidade de caracteres com o uso da função len()" )
print(nome.strip())
print(nome.count("")," Quantidede de carcteres incluindo espaço.")
nomeSemEspaco = nome.replace(" ", "")
print(nomeSemEspaco.count(""), " Quantidade de caracteres sem espaço.")
PrimeiroNome = nome.split(" ")
PrimeiroNome = PrimeiroNome[0]
print(PrimeiroNome)
print(len(PrimeiroNome))

