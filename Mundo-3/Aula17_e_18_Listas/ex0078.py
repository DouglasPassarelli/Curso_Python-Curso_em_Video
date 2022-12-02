'''
Faça um programa que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista.
'''

valores = list()
cont = maior = menor = posmaior = posmenor = 0
for c in range(0, 5):
    cont += 1
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
    if cont == 1:
        maior = valores[c]
        menor = valores[c]
    else:
        if maior <= valores[c]:
            maior = valores[c]
        if menor >= valores[c]:
            menor = valores[c]
print('-=' * 35)
print(f'Lista:{valores}')
print(f'O maior valor digitado foi {maior} na posição ', end=' ')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}...', end='')
print()








