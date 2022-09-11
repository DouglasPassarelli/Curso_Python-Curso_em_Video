print('-=' * 10, 'Sequencia de Numeros', '-=' * 10)
n = 1
soma = 0
quant = 0
print('Digite o tando de numeros que quiser e veja a soma entres eles e a quantidade de numeros digitados')
print('[DIGITE 999 PARA PARAR]')
while n != 999:
        n = int(input('Digite um numero: '))
        if n != 999:
            quant += 1
            soma += n
print('A quantidade de numero solicitados foram {} e a soma entre eles é {}'.format(quant, soma))
print('-=' * 10, 'Finalizado', '-=' * 10)

