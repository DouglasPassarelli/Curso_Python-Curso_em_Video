# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Considere R$ 3.27 = US$ 1

din = float(input('Quanto dinheiro voce tem? R$'))
dol = din / 4.28
eu = din / 5.12
print('Cotação dolar e de U$3.27')
print('A conversão de R${} em dolar e de U${:.2f} dolares'.format(din, dol))
print('Voce podera comprar U${:.2f} dolar'.format(dol))
print('Cotação euro e de EU$5.12')
print('A conversão de R${} em euro e de EU${:.2f}'.format(din, eu))
print('Voce podera comprar EU${:.2f} euros'.format(eu))
