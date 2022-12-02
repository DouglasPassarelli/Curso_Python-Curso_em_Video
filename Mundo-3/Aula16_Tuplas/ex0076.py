'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência
No final, mostre uma listagem de precos,
organizando os dados em forma tabular
'''

print('_' * 42)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('_' * 42)
listagem = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
for c in range(len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<33}', end='')
    if c % 2 == 1:
        print(f'R$ {listagem[c]:>6.2f}')
print('_' * 42)






