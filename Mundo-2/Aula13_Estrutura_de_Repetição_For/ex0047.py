# Crie um programa que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50

from time import sleep
print('-=' * 10, 'Contagem de Pares', '-=' * 10)
print('Segue a contagem dos numeros pares de 1 ate 50!')
for cont in range(1, 50 + 1):
    if cont % 2 == 0:
        sleep(0.3)
        print(cont, end=' ')
print('\nFINALIZADO')

