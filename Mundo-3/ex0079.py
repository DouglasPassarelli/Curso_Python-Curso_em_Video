valores = list()
while True:
    r = ''
    valor = (int(input('Digite um valor: ')))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar')
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar ? [S/N]: ')).upper().strip()[0]
    if r == 'N':
        break
print('-=' * 35)
print(f'Lista:{sorted(valores)}')


