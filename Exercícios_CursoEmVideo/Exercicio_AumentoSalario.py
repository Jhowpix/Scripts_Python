# Crie um algoritmo que acrecente 15% no salário atual de um funcionário

salario = float(input("Digite valor do salário atual para fazer um acréscimo de 15% no valor do salário R$ "))
print("Confirme valor salário atual R$: {:.2f}".format(salario))
print("Valor do sário com acréscimo de 15% será de R$ {:.2f}".format(salario + (salario * 15 / 100)))
# No Brasil queremos:
# 3.795,00 Ou seja:
# . para separar milhares
# , para separar centavos
# R$ para indicar Real

# VAMOS MELHORAR

print("Vamos para uma versão vom uma formatação melhor")
salario2 = float(input("Digite o valor do salário atual para fazer um acréscimo de 15% no valor do salário R$ "))
print(f"Confirme valor salário atual: R$ {salario2:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
novo_salario = salario2 + (salario2 * 15 / 100)
print(f"Valor do salário com acréscimo de 15% será de R$ {novo_salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
# Formatação explicada
# {salario2:,.2f}
#   ,  -> separa milhares
#   .2f -> mostra 2 casas decimais
# Exemplo:
# 3300 -> 3,300.00
# .replace(",", "X")
# Troca temporariamente a vírgula por "X".
# 3,300.00 -> 3X300.00
# .replace(".", ",")
# Troca o ponto por vírgula.
# 3X300.00 -> 3X300,00
# .replace("X", ".")
# Troca o "X" pelo ponto.
# 3X300,00 -> 3.300,00
# Resultado final:
# 3300 -> 3.300,00