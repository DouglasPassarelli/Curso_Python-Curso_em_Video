print('-=' * 10, 'PA usando while', '-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 1
while c <= 10:
    print('{} --> '.format(primeiro), end='')
    primeiro += razao
    c += 1
print('Finalizado', end='')
