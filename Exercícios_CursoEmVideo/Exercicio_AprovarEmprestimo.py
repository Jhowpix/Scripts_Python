# Crie um algoritmo que leia valor do imóvel desejado
# Valor da renda
# simule valores a parcelar por meses 120x (10 anos) 240x e 360x
# de um limite de crédito conforme a renda

# ESTUDO SOBRE JUROS

'''
Juros Simples J = C X i X t
Juros calculados apenas sobre o valor inicial. Pouco usado em financiamentos imobiliários.

Juros Compostos M=C×(1+i)t
Base da maioria dos financiamentos. Os juros incidem sobre o saldo atualizado.

Com correção pela TR SDn=SDn−1×(1+TR)×(1+i)
O saldo devedor é corrigido pela TR e depois recebe os juros do contrato.

Com correção pelo IPCA SDn=SDn−1×(1+IPCA)×(1+i)
O saldo é corrigido pela inflação (IPCA) e depois pelos juros.

Prestação fixa (Tabela Price) PMT=PV×i(1+i)n
                                      (1+i)n-1
Calcula parcelas iguais durante todos o financiamento.

Sistema SAC A=PV
              n
A amortização é fixa; as parcelas diminuem com o tempo.

Significado das letras
J = juros
C = capital inicial (valor financiado)
M = montante final
i = taxa de juros por período
t = tempo
SD = saldo devedor
PMT = valor da parcela
PV = valor presente (valor financiado)
n = número de parcelas
A = amortização

Taxa aproximada para referência
Financiamento imobiliário – taxas de mercado   cerca de 9%–13% ao ano
Taxa + TR   aproximadamente 9%–12% a.a. + TR
Taxa + IPCA    aproximadamente 5%–8% a.a. + IPCA
Prefixada    aproximadamente 10%–13% a.a.

NÃO EXISTE UMA REGRA FIXA PARA VALOR DE ENTRADA DE UM FINÂNCIAMENTO RESIDÊNCIAL

Financiamento: até cerca de 90% do imóvel em determinadas modalidades.
Entrada: consequentemente, pode partir de aproximadamente 10%.
Porém, em outras modalidades, a quota pode ser menor, exigindo 20%, 30% ou mais de entrada.
A própria CAIXA informa atualmente quota de até 90%, dependendo da modalidade, recursos e SAC/Price.

'''

while True:
    print('-'*20)
    print(' Sistema de simulação de finânciamento residêncial')
    print('-'*20)
    print('COM ESTE SISTEMA VOCÊ PODE SIMULAR. \n * Os valores das parcelas de um finânciamento. \n * Taxa de juros oferecidas ao ano pelos bancos. \n * Qual o valor que a sua renda libera de financiamento.')

    #Área somente para informações gerais sobre o sistema de financiamento residêncial nacional
    print()
    print('INFORMATIVO.\n * O Banco Central publica as taxas médias efetivamente praticadas pelas instituições,\n e os valores variam conforme a modalidade.')
    print(" * Entrada: ~10% a 30% do valor do imóvel. \n * Financiamento: valor restante. \n * Parcela: ~30% do valor da renda")
    print()

    # Coleta das informações para análise e cálculo do sistema
    print('Digite abaixo qual o valor do imóvel desejado.')
    valorImovel = float(input(' VALOR DO IMÓVEL R$: '))
    print()

    # Fórmulas para cálculos de taxa de entrada mais valor de finânciamento
    print(' ABAIXO VAMOS TE MOSTRAR UM EXEMPLO DE VALORES DE ENTRADAS BASEADO NAS PRINCIPAIS TAXAS USADAS ATUALMENTE.\n PARA MAIORES DUVIDAS CONSULTE O BANCO AO QUAL PRETENDE CONTRATAR O FINÂNCIAMENTO.')
    print()
    # Fórmula para entrada de 10%
    valorEntrada10p = valorImovel * 10 / 100
    print(f'VALOR DA ENTRADA TAXA DE 10%: R$ {valorEntrada10p:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."), f' VALOR DO FINANCIAMENTO R$ {valorImovel-valorEntrada10p:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    # Fórmula para entrada de 12%
    valorEntrada12p = valorImovel * 12 / 100
    print(f'                         12%: R$ {valorEntrada12p:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."), f'                        R$ {valorImovel-valorEntrada12p:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    # Fórmula para entrada de 14%
    valorEntrada14p = valorImovel * 14 / 100
    print(f'                         14%: R$ {valorEntrada14p:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."), f'                        R$ {valorImovel-valorEntrada14p:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    # Fórmula para entrada de 15%
    valorEntrada15p = valorImovel * 15 / 100
    print(f'                         15%: R$ {valorEntrada15p:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."), f'                        R$ {valorImovel-valorEntrada15p:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    # Fórmula para entrada de 20%
    valorEntrada20p = valorImovel * 20 / 100
    print(f'                         20%: R$ {valorEntrada20p:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."), f'                        R$ {valorImovel-valorEntrada20p:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    # Fórmula para entrada de 30%
    valorEntrada30p = valorImovel * 30 / 100
    print(f'                         30%: R$ {valorEntrada30p:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."), f'                        R$ {valorImovel-valorEntrada30p:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))

    # Coleta valor da renda
    print()
    print(' * COM BASE NA SUA RENDA CONSEGUIMOS SIMULAR O VALOR DISPONÍVEL PARA FINANCIAMENTO. \n Informe abaixo sua renda atual. ')
    valorRenda = float(input('RENDA: '))
    print()
    print(" O financiamento considera até 30% da renda mensal para a parcela.\n O valor liberado varia conforme renda, prazo e taxa de juros.")
    print()

    # Fórmula para valores disponíveis de crédito para finânciamento
    juros = 0.11 * 12 / 100
    prazo = 360
    parcela = valorRenda * 30 / 100
    credito = parcela * ((1 - (1 + juros) ** -prazo) / juros)

    print(f"Crédito estimado: R$ {credito:,.2f}")
    print(f"Parcela de referência: R$ {parcela:,.2f}")
    print("Prazo máximo considerado: 360 meses")
    print()

    # Informativo
    print(" * O crédito é definido pela renda, mas o financiamento também. \n * Depende do percentual do imóvel que o banco aceita financiar. \n * Por isso, mesmo com crédito disponível, pode ser necessária uma entrada. ")
    print()

    # Fórmulas para mostrar possíveis planos de financiamento baseado no valor do imóvel e na renda apresentada

    jurosTaxaTR = 0.11 * 12 / 100
    jurosIPCA = 0.09 * 12 /100
    jurosPreFixado = 0.13 * 12 /100

    valorParcelaImovel = (valorImovel - valorEntrada10p) / 120
    valorJurosDaParcela120 = ((valorImovel - valorEntrada10p) / 120) * jurosTaxaTR
    valorTotalParcela120 = valorParcelaImovel + valorJurosDaParcela120

    valorParcelaImovel = (valorImovel - valorEntrada10p) / 240
    valorJurosDaParcela240 = ((valorImovel - valorEntrada10p) / 240) * jurosTaxaTR
    valorTotalParcela240 = valorParcelaImovel + valorJurosDaParcela240

    valorParcelaImovel = (valorImovel - valorEntrada10p) / 360
    valorJurosDaParcela360 = ((valorImovel - valorEntrada10p) / 360) * jurosTaxaTR
    valorTotalParcela360 = valorParcelaImovel + valorJurosDaParcela360

    print('* Taxa de juros TR (Taxa Referêncial) em 11% ao ano.')
    print(f'Valores das parcelas simuladas para 120 meses R$ {valorTotalParcela120:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    print(f'                                    240 meses R$ {valorTotalParcela240:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    print(f'                                    360 meses R$ {valorTotalParcela360:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))

    valorJurosDaParcela120 = ((valorImovel - valorEntrada10p) / 120) * jurosIPCA
    valorTotalParcela120TR = valorParcelaImovel + valorJurosDaParcela120

    valorJurosDaParcela240 = ((valorImovel - valorEntrada10p) / 240) * jurosIPCA
    valorTotalParcela240TR = valorParcelaImovel + valorJurosDaParcela240

    valorJurosDaParcela360 = ((valorImovel - valorEntrada10p) / 360) * jurosIPCA
    valorTotalParcela360TR = valorParcelaImovel + valorJurosDaParcela360

    print()
    print(' * Taxa de juros IPCA (Juros do banco + correção do saldo devedor pela inflação) em 9% ao ano.')
    print(f'Valores das parcelas simuladas para 120 meses R$ {valorTotalParcela120TR:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    print(f'                                    240 meses R$ {valorTotalParcela240TR:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    print(f'                                    360 meses R$ {valorTotalParcela360TR:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))

    valorJurosDaParcela120 = ((valorImovel - valorEntrada10p) / 120) * jurosPreFixado
    valorTotalParcela120Pre = valorParcelaImovel + valorJurosDaParcela120

    valorJurosDaParcela240 = ((valorImovel - valorEntrada10p) / 240) * jurosPreFixado
    valorTotalParcela240Pre = valorParcelaImovel + valorJurosDaParcela240

    valorJurosDaParcela360 = ((valorImovel - valorEntrada10p) / 360) * jurosPreFixado
    valorTotalParcela360Pre = valorParcelaImovel + valorJurosDaParcela360

    print()
    print(' * Taxa de juros préfixado em 13% ao ano.')
    print(f'Valores das parcelas simuladas para 120 meses R$ {valorTotalParcela120Pre:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    print(f'                                    240 meses R$ {valorTotalParcela240Pre:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    print(f'                                    360 meses R$ {valorTotalParcela360Pre:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))

    # Mostrar para usuario valore de parcelar que cabem no seu financiamento
    if parcela <= valorTotalParcela120 or valorTotalParcela120TR or valorTotalParcela120Pre:
        print()
        print()
        print('SEU CREDITO É LEGÍVEL A PARTIR DE ALGUMAS LINHAS DE CREDITO DE 120 MESES CONFIRA!!!.')
    elif parcela <= valorTotalParcela240 or valorTotalParcela240TR or valorTotalParcela120Pre:
         print('SEU CREDITO É LEGÍVEL A PARTIR DE ALGUMAS LINHAS DE CREDITO DE 240 MESES CONFIRA!!!.')
    elif parcela <= valorTotalParcela360 or valorTotalParcela360TR or valorTotalParcela360Pre:
        print('SEU CREDITO É LEGÍVEL A PARTIR DE ALGUMAS LINHAS DE CREDITO DE 360 MESES CONFIRA!!!.')
    else:
        print('Infelizmente nenhuma das opções simuladas bate com sua linha de credito.')

    print(f'O VALOR DA SUA PARCELA DE REFERÊNCIA É R$ {parcela:,.2f}')
    print()
    print('-'*20)
    #PARAR AQUI
    break