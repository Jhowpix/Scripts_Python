# Faça um programa que leia comprimento do cateto oposto
# e do cateto adjacente de um triângulo retêtangulo, calcule e mostre o comprimento da hipotenusa


'''
 Lembrando a matéria
 O qué um truângulo retângulo?
 É um triângulo que possui um ângulo de 90 graus

 Ele possui três lados:

    Hipotenusa → é sempre o lado oposto ao ângulo de 90° e é o maior lado.
    Cateto oposto → fica do lado contrário ao ângulo que estamos analisando.
    Cateto adjacente → fica ao lado do ângulo que estamos analisando.

'''
import math

CatetoOposto = float(input("Digite o valor do cateto oposto: "))
CatetoAdjacente = float(input("Digite o valor do cateto adjacente: "))
Hipotenusa = math.hypot(CatetoAdjacente,CatetoOposto)
print("Hipotenusa: {:.2f}".format(Hipotenusa))

# Faça um programa que leia um numero qualquer
# atribua ele a um ângulo e mostre
# o valor do seno, cosseno e tangente desse ângulo

Angulo = float(input("Digite o valor do angulo: "))
Angulo = math.radians(Angulo)
print("Angulo: {:.2f}".format(Angulo))
print("O valor de seno {:.2f} ".format(math.sin(Angulo)))
print("O valor de cosseno {:.2f} ".format(math.cos(Angulo)))
print("O valor de tangente {:.2f} ".format(math.tan(Angulo)))