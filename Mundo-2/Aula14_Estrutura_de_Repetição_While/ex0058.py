''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer
'''

from time import sleep
from random import randint


palpite = 0
print('-=' * 10, 'Jogo Da Advinhação v2.0', '-=' * 10)
computador = randint(1, 10)
print('Vou pensar em um numero de 0 a 10 tente acertar!')
print('pensando...')
sleep(2)
jogador = int(input(('Qual numero eu pensei ? R: ')))
while computador != jogador:
    print('Voce errou tente novamente! O computador jogou {} e voce jogou {}'.format(computador, jogador))
    jogador = int(input('Proximo palpite: '))
    palpite += 1
print('O computador jogou {} e voce {} voce ganhou!'.format(computador, jogador))
print('Parabens!! Vocé venceu o computador')
print('Voce teve um total de {} palpites ate advinhar'.format(palpite))
