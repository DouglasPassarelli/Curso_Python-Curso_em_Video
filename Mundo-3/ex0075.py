'''n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite um terceiro numero: '))
n4 = int(input('Digite um ultimo numero: '))
numeros = (n1, n2, n3, n4)
cont9 = cont = 0
print(f'Os numeros listados forma: {numeros}')
for c in numeros:
    if c == 9:
        cont9 += 1
    if c % 2 == 0:
        print(c, end=' --> ')
        cont += 1
if cont >= 1:
    print('Foram os valores Pares digitados')
else:
    print('Nenhum valor par foi digitado!')
print(f'O numero 9 apareceu {cont9} vezes ')
if 3 in numeros:
    print(f'O numero 3 esta na {numeros.index(3) + 1}ª posição')
else:
    print('O numero 3 não foi digitado em nenhuma posição')
print('Finalizado')'''

#codigo do Guanabara

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
