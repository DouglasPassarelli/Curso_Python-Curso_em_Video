''' Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
'''

print('-=' * 10, 'Tabuada v3.0', '-=' * 10)
resultado = 0
while True:
    n = int(input('Digite um numero na qual queira ver a tabuada ? '))
    print('=' * 45)
    if n > 0: #ao ser substituido este if pode ser descartado
        for c in range(1, 11):
            resultado = n * c
            print(f'{n} X {c} = {resultado}')
        print('=' * 45)
    if n < 0: # substituindo este if pelo de cima funciona corretamente
        break
print('Progama de Tabuada encerrado!')
print('\033[31m-=' * 10, 'Volte Sempre', '-=' * 10)
