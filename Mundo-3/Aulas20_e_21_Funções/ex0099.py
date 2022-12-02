''' 
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

from time import sleep
def maior (* num):
    print('-=' * 20)
    print('Analisando os valores passados....')
    m = 0
    for c in num:
        if c >= m:
            m = c
        print(c, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo!')
    print(f'O maior valor informado foi o {m}')


maior(5, 6, 3, 2, 4, 8, 10, 3)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
