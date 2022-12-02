'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep
gerador = list()
sorteio = list()
print('-=' * 20)
print('{:^40}'.format(' JOGOS DA MEGA SENA '))
print('-=' * 20)
palpite = int(input('Quantos jogos voce quer que eu sorteie ? '))
print('{:=^41}'.format(f' Sorteando {palpite} Jogos '))
for c in range(0, palpite):
    while True:
        valor = randint(1, 60)
        if valor not in gerador:
            gerador.append(valor)
        if len(gerador) == 6:
            break
    sorteio.append(gerador[:])
    gerador.clear()
    print(f'Jogo {c+1}: {sorted(sorteio[c])}')
    sleep(1)
print('>>>' * 5, 'BOA SORTE', '<<<' * 5)




