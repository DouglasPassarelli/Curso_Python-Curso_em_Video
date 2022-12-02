''' Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

cadastro = []
while True:
    soma = 0
    jogadores = {}
    listagem = []
    r = ''
    print('-' * 40)
    jogadores['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {jogadores["nome"]} fez ? '))
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols fez na {c} partida ? '))
        listagem.append(gols)
        jogadores['gols'] = listagem[:]
        soma += gols
    jogadores['total'] = soma
    cadastro.append(jogadores.copy())
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while r not in 'NnSs':
        print('ERRO! Por favor digite apenas S ou N')
        r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r in 'Nn':
        break
print('-=' * 20)
print('cod', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for p, c in enumerate(cadastro):
    print(f'{p:>3} ', end='')
    for v in c.values():
        print(f'{str(v):<15}', end='')
    print()
print('-' * 40)
while True:
    dados = int(input('Mostrar dados de qual jogador (999 para parar)? '))
    if dados > len(cadastro) and dados != 999:
        print(f'Erro! Jogador nao existe, nao existe jogador com o numero {dados}!!!')
    for p, c in enumerate(cadastro):
        if dados == p:
            print(f'-- LEVANTAMENTO DO JOGADOR: {c["nome"]}')
            for go, g in enumerate(c['gols']):
                print(f'No jogo {go}, fez {g} gols.')
    print('-' * 40)
    if dados == 999:
        break
print('>>> FINALIZADO <<<')

