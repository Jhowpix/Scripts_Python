# Crie um código que pegue atlura da parede
# largura da parede mostre sua rea
# e informe quantos litros de tinta sera necessario
# para pintar aquela area levando em conta que cada litro
# de para pintar 2 metros quadrados


AlturaParede = float(input("Digite a altura da parede: "))
LarguraParede = float(input("Digite a largura da parede: "))
areaParede = AlturaParede * LarguraParede
tinta = areaParede / 2
print("A área é de: ", areaParede, " ira precisar de", tinta, "litros")