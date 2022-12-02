'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da Chapecoense
'''

times = ('Palmeiras', 'Athletico-PR', 'Atletico-MG', 'Corinthians', 'Internacional', 'Fluminense', 'São Paulo', 'Flamengo', 'Botafogo', 'Santos', 'Avai', 'Coritiba', 'America-MG', 'Bragantino', 'Ceara SC', 'Atletico-GO', 'Goias', 'Cuibá', 'Juventude', 'Fortaleza')
print('{:=^40}'.format(' Tabela do Brasileirão '))
print(f'Times do Brasileirão: {times}')
print('-=' * 50)
print(f'Os 5 primeiros colocados da tabela são: {times[:5]}')
print('-=' * 50)
print(f'Os ultimos 4 colocados da tabela são: {times[-4:]}')
print('-=' * 50)
print(f'A tabela em ordem alfabetica ficará: {sorted(times)}')
print('-=' * 50)
print('O time do Botafogo esta na posição: {}º'.format(times.index('Botafogo')))


