# Crie um algoritmo que some o valor da diária de um veiculo
# mais o valor por kilometros rodados
# levando em consideração que o valor da diária é de R$60,00
# e o valor do kilometro é de R$0,15 centavos

Veiculo = float(input("Informe quantos dias o veiculo ficou alugado ?"))
Veiculo = Veiculo*60
Kilometros = float(input("Informe quantos kilometros foram percorridos ?"))
Kilometros = Kilometros*0.15
Valor = Veiculo + Kilometros
print(f"O valor a ser pago é de por dia R$ {Veiculo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"Valor a ser pago por R$ {Kilometros:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"Valor total a ser pago de R$ {Valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))