''' Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''

from datetime import date


data = date.today().year
maior = 0
menor = 0
for c in range(1, 7+1):
    nasc = int(input('Digite o ano de nasc da {}° pessoa: '.format(c)))
    idade = data - nasc
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('um total de {} pessoas atingiram a maioridade'.format(maior))
print('Um total de {} pessoas ainda nao atingiram a maioridade'.format(menor))
