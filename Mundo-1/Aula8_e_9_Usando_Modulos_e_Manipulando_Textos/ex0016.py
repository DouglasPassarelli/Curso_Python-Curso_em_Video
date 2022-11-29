# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc
real = float(input('Digite um valor real: '))
print('O valor inteiro de {} e de {}'.format(real, trunc(real)))




