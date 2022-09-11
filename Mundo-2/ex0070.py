print('=' * 35)
print('          Lojas do Dogão')
print('=' * 35)
total = quant = 0
maisbarato = total = quant = cont = 0 # Gambiarra para ver o menor preço
produto = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Qual o valor do produto: R$ '))
    cont += 1
    print('=' * 35)
    total += preco
    if preco > 1000:
        quant += 1
    if cont == 1 or preco < maisbarato:
        maisbarato = preco
        produto = nome
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    print('=' * 35)
    if r == 'N':
        break
print(f'O total gasto foi de R${total:.2f} nas compras')
print(f'No total foram {quant} produtos que custão mais de R$1000,00')
print(f'O nome do produto mais barato é {produto} que custa R${maisbarato:.2f}')