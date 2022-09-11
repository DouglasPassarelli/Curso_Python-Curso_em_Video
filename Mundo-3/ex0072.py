extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print('-=' * 10, 'Numeros Extensos', '-=' * 10)
while True:
    n = int(input('Digite um numero de [0 a 20]: '))
    while n < 0 or n > 20:
        n = int(input('Tente Novamente! Digite um numero de [0 a 20]: '))
    print(f'O numero {n} por extenso é {extenso[n]}')
    r = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 10, 'Finalizado', '-=' * 10)







