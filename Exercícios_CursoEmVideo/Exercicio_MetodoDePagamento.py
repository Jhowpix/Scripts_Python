'''

Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço normal
– 3x ou mais no cartão: 20% de juros

'''
while True:
    print('-'*30)
    print('{:^30}'.format(' PROGRAMA DE PAGAMENTO '))
    print('-'*30)
    valorProduto = float(input('Digite o valor do produto: '))
    print('''          OPÇÕES DE PAGAMENTO.
            [1]  Á vista dinheiro/cheque: 10% de desconto.
            [2]  Á à vista no cartão: 5% de desconto.
            [3]  Em até 2x no cartão: preço normal.
            [4]  Em 3x ou mais no cartão: 20% de juros.
    ''')
    formaPagamento = int(input('Digite o tipo de pagamento: '))
    if formaPagamento == 1:
        valorProduto = valorProduto - (valorProduto * 0.10)
        print(f'Valor do produto com 10% de desconto. \n Pagamento a vista : R$ {valorProduto:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    elif formaPagamento == 2:
        valorProduto = valorProduto - (valorProduto * 0.05)
        print(f'Valor do produto com 5% de desconto. \n Pagamento a vista no cartão R$ {valorProduto:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    elif formaPagamento == 3:
        print(f'Valor do produto R$ {valorProduto:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
        valorParcela = valorProduto / 2
        print(f'Valor dividido em 2 vezes. \nValor da parcela R$ {valorParcela:,.2f}'.replace(",", "y").replace(".", ",").replace("y", "."))
    elif formaPagamento == 4:
        x = int(input('''   Escolha o número de parcelas.
        
[1]  
[2]  
[3]  
[4] 
[5] 
[6]  

    Você pode dividir em até 6 vezes.
        '''))
        valorProduto = valorProduto + (valorProduto * 0.20)
        valorParcela = valorProduto / x
        print('Valor dividido em vezes {}'.format(x))
        print(f'Valor da parcela R$ {valorParcela:,.2f}'.replace(",", "y").replace(".",",").replace("y", "."))
    else:
        print('{:^30}'.format('FORMA DE PAGAMENTO ESCOLHIDA INVALIDA!'))
    print()

