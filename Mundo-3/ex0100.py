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

