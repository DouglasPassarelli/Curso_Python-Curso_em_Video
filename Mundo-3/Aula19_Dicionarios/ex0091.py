'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
cont = 1
print('Valores Sorteados:')
for k, v in jogadores.items():
    print(f'   O {k} jogou: {v}')
    sleep(1)
print('Ranking dos Jogadores:')
for k, v in sorted(jogadores.items(), key=lambda item: item[1], reverse=True):
    print(f'   {cont}º lugar: {k}: {v}')
    sleep(1)
    cont += 1




