valores = list()
cont = 0
while True:
    r = ' '
    valores.append(int(input('Digite um valor: ')))
    cont += 1
    while r not in 'NnSs':
        r = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if r in 'Nn':
        break
print('-=' * 25)
print(f'Foram digitados {cont} valores')
valores.sort(reverse=True)
print(f'A lista em ordem decrescente ficara: {valores} ')
if 5 in valores:
    print(f'O valor 5 esta na lista, e esta na posição {valores.index(5)}')
else:
    print('O valor 5 nao se encontra na lista!')
print('Finalizado')