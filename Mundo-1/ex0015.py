dias = int(input('Quantos dias foi alugado? '))
km = float(input('Quantos km rodados? '))
aldias = dias * 60
pkm = km * 0.15
print('O total a pagar e de R${:.2f}'.format(aldias + pkm))
