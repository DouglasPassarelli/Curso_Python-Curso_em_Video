''' Faça um programa que leia o peso de cinco pessoas
No final, mostre qual foi o maior e o menor peso lidos'''

maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa: '.format(pessoas)))
    if pessoas == 1: # atribuindo a primeira pessoa o valor maior e o valor menor, depois fazendo a comparação
        maior = peso
        menor = peso
    else:
        if peso >= maior:
            maior = peso
        if peso <= menor:
            menor = peso
print('O maior peso foi {}Kg'.format(maior))
print('O menor peso foi {}Kg'.format(menor))


