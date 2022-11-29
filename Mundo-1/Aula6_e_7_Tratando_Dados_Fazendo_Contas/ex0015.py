# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias # pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado


dias = int(input('Quantos dias foi alugado? '))
km = float(input('Quantos km rodados? '))
totaldias = dias * 60
pkm = km * 0.15
print('O total a pagar e de R${:.2f}'.format(totaldias + pkm))
