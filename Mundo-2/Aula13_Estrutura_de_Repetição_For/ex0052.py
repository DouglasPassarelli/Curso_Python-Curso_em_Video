''' Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo'''

print('-=' * 10, 'Numeros Primos', '-=' * 10)
num = int(input('Digite um numero: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0: #colocando cor nos numeros que sao divisiveis
        print('\033[31m', end='')
        cont = cont + 1  #atribuindo a uma variavel o numero de divisoes feitas
    else:
        print('\033[33m', end='')
    print('{} '.format(c), end='')


if cont > 2:
    print('\033[m \nO numero {} foi divisivel {} vezes'.format(num, cont))
    print('E por isso ele nao e um numero primo')
else:
    print('\033[m \nO numero {} foi divisivel {} vezes'.format(num, cont))
    print('E por isso ele e um numero primo')







