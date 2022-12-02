'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''


princ = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite {c}º valor: '))
    if valor % 2 == 0:
        princ[0].append(valor)
    else:
        princ[1].append(valor)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(princ[0])}')
print(f'Os valores impares digitados foram: {sorted(princ[1])}')





