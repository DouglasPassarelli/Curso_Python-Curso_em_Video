'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''

print('\033[4;31m-=' * 10, 'Lojas Do Dogão', '-=' * 10)
preço = float(input('\033[32mQual e o valor dos produto ? R$'))
print('''Qual a condição de pagamento ?
[1] (a vista) 10% de desconto
[2] (cartão)  5% de desconto
[3] (2x no cartão) sem desconto
[4] (3x ou mais no cartão) 20% de jutos ''')
condicao = int(input('Sua Opção: \033[m'))
if condicao == 1:
    desconto = preço * 10 / 100
    npreço = preço - desconto
    print('\033[34mO valor do produto de R${:.2f}, saira no valor de R${:.2f} á vista'.format(preço, npreço))
elif condicao == 2:
    desconto = preço * 5 / 100
    npreço = preço - desconto
    print('\033[34mO valor do produto de R${:.2f}, saira no valor de R${:.2f} no cartão'.format(preço, npreço))
elif condicao == 3:
    parcela = preço / 2
    print('Sua compra parcelada em 2x ficará R${:.2f} no cartão'.format(parcela))
    print('\033[34mO valor total ficara em {:.2f} pois nessa modalidade nao tem desconto'.format(preço))
elif condicao == 4:
    parcela = int(input('\033[34mQuantas parcelas? '))
    juros = preço * 20 / 100
    npreço = preço + juros
    valorparcela = npreço / parcela
    print('A parcela do produto ficara R${:.2f} em {} parcelas'.format(valorparcela, parcela))
    print('O produto no valor de R${:.2f} parcelado,\nficara no valor total de R${:.2f} com 20% de juros nessa modalidade'.format(preço, npreço))
else:
    print('\033[34mOpção invalida, tente novamente!')
    print('Sua compra de R${:.2f}, ficara R${:.2f} no final'.format(preço, preço))
print('\033[4;31m-=' * 10, 'TERMINADO', '-=' * 10)

