'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint
from time import sleep
def sorteio(num):
    cont = 0
    print('Sorteando os 5 numeros:', end='')
    while cont < 5:
        num.append(randint(1, 10))
        print(num[cont], end=' ')
        sleep(0.5)
        cont += 1
    print('Pronto!')


def somapar(num):
    soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
    print(f'A soma de todos os valores pares de {num} é {soma}')


numeros = []
sorteio(numeros)
somapar(numeros)

