print('-=' * 10, 'Tabuada v2.0', '-=' * 10)
n = int(input('Digite um numero na qual queira ver a tabuada: '))
resultado = 0
for cont in range(1, 11):
    resultado = cont * n
    print('{} X {:2} = {}'.format(n, cont, resultado))
print('-=' * 10, 'FINALIZADO', '-=' * 10)
