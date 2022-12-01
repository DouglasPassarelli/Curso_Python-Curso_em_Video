#Faça um programa que leia um número qualquer e mostre
#o seu fatorial 

# A fatorial do ultimo numero * o numero seguinte corresponde a o fatorial daquele numero
# EX: fatorial de 4*3*2*1 = 24, 24 * 5 = 120 que e o fatorial do numero 5, fatorial de 5! = 120


'''print('-=' * 10, 'Fatorial', '-=' * 10)
n = int(input('Digite um numero na qual queira ver seu fatorial: '))
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f = f * c
print('{}'.format(f))'''


#condição while
'''print('-=' * 10, 'Fatorial', '-=' * 10)
n = int(input('Digite um numero na qual queira ver o fatorial: '))
f = 1
c = n
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f), end='')'''


#condição com while e com for
print('-=' * 10, 'Fatorial', '-=' * 10)
n = int(input('Digite um numero na qual queira ver o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0: #ENQUANTO C = 1 FOR MENOR OU IGUAL A N = 5 FAÇA
    for cont in range(n, 0, -1): #PARA CONT = CONTADOR
         print('{}'.format(cont), end='')
         print(' X ' if c > 1 else ' = ', end='')
         f *= cont
         c -= 1
print('{}'.format(f), end='')


'''from math import factorial
n = int(input('Digite um numero na qual queria ver seu fatorial:'))
f = factorial(n)
print('O fatorial de {}! e igual a {}'.format(n, f))'''








