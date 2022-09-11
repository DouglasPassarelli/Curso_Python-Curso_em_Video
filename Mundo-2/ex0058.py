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


#codigo do guanabara

'''from random import randint
print('Sou seu computator... Vou pensar em um numero de 0 a 10')
print('Tente adivinhar!')
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite ?'))
    palpites += 1
    if computador == jogador:
        acertou = True
    else:
        if computador > jogador:
            print('Mais... Tente outra vez!')
        elif computador < jogador:
            print('Menos... Tente outra vez!')
print('Parabens! Voce acertou com {} palpites'.format(palpites))'''



