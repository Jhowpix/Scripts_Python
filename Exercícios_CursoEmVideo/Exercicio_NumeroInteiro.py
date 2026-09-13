# Crie um programa que leia um numero qualquer
# e retore somente o inteiro

inteiro = float(input("Digite o valor para obter o inteiro : "))
print("O valor inteiro é: {}".format(inteiro.__trunc__()))

# alêm da função __trunc__ temos o int() que retornaria o mesmo valor