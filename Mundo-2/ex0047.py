from time import sleep
print('-=' * 10, 'Contagem de Pares', '-=' * 10)
print('Segue a contagem dos numeros pares de 1 ate 50!')
for cont in range(1, 50 + 1):
    if cont % 2 == 0:
        sleep(0.3)
        print(cont, end=' ')
print('\nFINALIZADO')

#segunda opção
#for cont in range(2, 51, 2):
