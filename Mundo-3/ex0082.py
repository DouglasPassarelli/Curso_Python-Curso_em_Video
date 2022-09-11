valores = list()
par = list()
impar = list()
while True:
    r = ' '
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    while r not in 'SsNn':
        r = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 20)
print(f'A lista completa dos valores sao:{valores}')
for c in valores:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'A lista com valores pares são:{par}')
print(f'A lista com valores impares são:{impar}')
