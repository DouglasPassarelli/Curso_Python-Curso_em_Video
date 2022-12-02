'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:
a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
b) quais foram os números pares
'''

numeros = (int(input('Digite um numero: ')),
           int(input('Digite outro numero: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite o ultimo numero: ')))
print(f'Os numeros listados foram:{numeros}')
print(f'O numero 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 aparece na {numeros.index(3)+1}ª posição')
else:
    print('O numero 3 nao foi encontrado em nenhuma posição!')
print('Os numeros pares digitados foram ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
