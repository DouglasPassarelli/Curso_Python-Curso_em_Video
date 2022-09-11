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



#codigo do enunciado dado pelo guanabara

'''somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('------- {}° PESSOA --------'.format(p))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo: M/F '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é {} anos '.format(mediaidade))
print('O homem mais velho do grupo com {} se chama {}'.format(maioridadehomem, nomevelho))
print('Tem um total de {} mulheres com menos de 20 anos'.format(totmulher20))'''













