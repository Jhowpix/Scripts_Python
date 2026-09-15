# Escreva um programa que leia a velocidade de um carro
# se ele ultrapassar 80km/h mostre uma mensagem dizendo
# que ele foi multado
# A multa vai custar R$7,00 por cada Km acima do limite
from http.cookiejar import uppercase_escaped_char
while True:
    print("_"*12)

    TextoTitulo = "Sistema de Transito Brasileiro"
    TextoTitulo = TextoTitulo.upper()
    print(TextoTitulo)
    print()
    TextoInformativo = " Para auxiliar  no sistema de controle de transito\n vamos calcular de forma automática o valor da multa.\n Para o uso do sistema informe a velocidade permitida da via e a velocidade do veiculo. "
    print(TextoInformativo)
    print()

    ValorLimiteVia = int(input("Informe o valor limite da via: "))

    VerificandoInformacao = input(str("Confirma velocidade de via {} Km/h \n Para confirmar digite ( S ) \n Para digitar a velocidade limite novamente digite ( N )\n ".format(ValorLimiteVia))).strip().upper()

    if VerificandoInformacao == "S":
        ValorVelocidadeVeiculo = int(input("Informe a velocidade do veiculo: "))
        print(" VELOCIDADE DO VEICULO {} Km/h".format(ValorVelocidadeVeiculo))
        if ValorLimiteVia >= ValorVelocidadeVeiculo:
            print(" Veiculo dentro do limite permitido pela via")
        else:
            VelocidadeExcedida = ValorVelocidadeVeiculo - ValorLimiteVia
            ValorDaMulta = (ValorVelocidadeVeiculo - ValorLimiteVia) * 7
            print(" Velocidade excedida em {}Km/h\n Valor a ser pago é de R$ {:.2f}".format(VelocidadeExcedida,ValorDaMulta))

    elif VerificandoInformacao == "N":
        continue
    else:
        print("Carácter digitado invalido")
