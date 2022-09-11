'''print('-=' * 10, 'Super PA', '-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
quantidade = 0
c = 1
while c <= 10:
    print('{} --> '.format(primeiro), end='')
    primeiro += razao
    quantidade += 1
    c += 1
print('Pausa')
termo = 1
while termo != 0:
    termo = int(input('Deseja ver mais quantos termo? R:'))
    for cont in range(1, termo + 1):
        print('{} --> '.format(primeiro), end='')
        primeiro += razao
        quantidade += 1
    if termo != 0:
        print('Pausa')
print('A progressão foi finalizada com {} termos mostrados'.format(quantidade))'''


#codigo do guanabara

'''primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
quantidade = 0
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} --> '.format(primeiro), end='')
        primeiro += razao
        quantidade += 1
        c += 1
    print('Pausa')
    mais = int(input('Deseja ver mais quantos termos? '))
print('A progressão foi finalizada com {} termos mostrados'.format(quantidade))'''




