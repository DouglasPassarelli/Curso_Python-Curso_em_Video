''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''

hvelho = ''
maior = 0
totm = 0
mediaidade = 0
for p in range(1, 5):
    nome = str(input('Escreva seu nome: ')).strip()
    idade = int(input('Quantos anos voce tem: '))
    sexo = str(input('Qual o seu sexo ? [M] OU [F]')).strip().upper()
    print('-=' * 20)
    mediaidade += idade
    if sexo in 'Fm':
        if idade < 20:
            totm = totm + 1
    elif sexo in 'Mm':
        if idade >= maior:
            maior = idade
            hvelho = nome

mediaidade = int(mediaidade / 4)
print('A média de idade do grupo é {} anos'.format(mediaidade))
print('O nome do homem mais velho tem {} anos e se chama {}'.format(maior, hvelho))
print('Tem um total de {} mulheres com menos de 20 anos'.format(totm))














