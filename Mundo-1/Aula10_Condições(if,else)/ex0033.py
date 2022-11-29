#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

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










