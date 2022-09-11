from time import sleep
print('=' * 10, 'PAR OU IMPAR', '=' * 10)
num = int(input('Digite um numero:'))
print('Vamos verificar se {} e "PAR" ou "IMPAR"'.format(num))
print('Processando...')
sleep(2.5)
if num % 2 == 0:
    print('O numero {} é Par'.format(num))
else:
    print('O numero {} é IMPAR'.format(num))
print('=' * 12, 'TERMINADO', '=' * 12)

