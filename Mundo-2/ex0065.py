r = ''
maior = menor = quant = soma = media = 0

while r != 'N':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N] R: ')).strip().upper()[0]
    quant += 1
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if n >= maior:
            maior = n
        if n <= menor:
            menor = n
media = soma / quant
print('O maior numero foi {}, e o menor numero foi {}'.format(maior, menor))
print('Voce digitou {} numeros e a media entre eles foi de {}'.format(quant, media))
print('-=' * 10, 'Finalizado', '-=' * 10)