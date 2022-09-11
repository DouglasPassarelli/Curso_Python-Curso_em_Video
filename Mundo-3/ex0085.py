'''princ = list()
par = list()
impar = list()
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
princ.append(par[:])
par.clear()
princ.append(impar[:])
impar.clear()
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(princ[0])}')
print(f'Os valores impares digitados forma: {sorted(princ[1])}')'''

#Segunda Forma mais simples
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





