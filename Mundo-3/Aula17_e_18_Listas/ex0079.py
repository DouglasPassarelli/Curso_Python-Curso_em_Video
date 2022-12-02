'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

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


