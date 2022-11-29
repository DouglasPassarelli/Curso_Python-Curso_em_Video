# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

#metros = int(input('Quantos metros tem:'))
#cen = metros * 100
#mi = metros * 1000
#print('O valor de {} metros convertido para centimetros e de {} centimetros'.format(metros, cen))
#print('O valor de {} convertido para milimetros e de {} milimetros'.format(metros, mi))

#Conversão de metros para kilômetros, hectômetros, decâmetros, decímetros, centímetros e milímetros.

metros = float(input('Uma distancia em metros:'))
print('A medida de {}m corresponde a'.format(metros))
ki = metros / 1000
he = metros / 100
de = metros / 10
dec = metros * 10
cen = metros * 100
mil = metros * 1000
print(' {}km\n {}hm\n {}dam\n {}dm\n {}cm\n {}mm'.format(ki, he, de, dec, cen, mil))