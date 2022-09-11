'''n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
n3 = int(input('Digite um terceiro numero:'))
print('Qual numero e maior, e qual numero e menor entre {}, {}, {}'.format(n1, n2, n3))
# Verificando qual o valor menor
if n1 <= n2 and n1 <= n3:
    print('O menor numero é {}'.format(n1))
if n2 <= n1 and n2 <= n3:
    print('O menor numero é {}'.format(n2))
if n3 <= n1 and n3 <= n2:
    print('O menor numero é {}'.format(n3))
#Verificando qual o valor maior
if n1 >= n2 and n1 >= n3:
    print('O maior numero é {}'.format(n1))
if n2 >= n1 and n2 >= n3:
    print('O maior numero é {}'.format(n2))
if n3 >= n1 and n3 >= n2:
    print('O maior numero é {}'.format(n3))
print('=' * 10, 'Terminado', '=' * 10)'''

#Segunda opçao mais simplificada


n1 = int(input('Primeiro numero:'))
n2 = int(input('Segundo numero:'))
n3 = int(input('Terceiro numero:'))
#Verificando com o valor menor
menor = n1
if n2 < n1 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificando qual valor e o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior numero é {}'.format(menor))
print('O menor numero é {}'.format(maior))
print('=' * 10, 'Terminado', '=' * 10)










