dados = {}
listagem = []
soma = 0
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas o {dados["nome"]} jogou ? '))
print('{:=^35}'.format(' Contador de gols '))
for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c} ? '))
    listagem.append(gols)
    soma += gols
dados['gols'] = listagem[:]
dados['total'] = soma
print('-=' * 35)
print(dados)
print('-=' * 35)
for k, v in dados.items():
    print(f'O campo {k} tem o valor de {v}.')
print('-=' * 35)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for p, c in enumerate(dados['gols']):
    print(f'   => Na partida {p}, fez {c} gols.')
print(f'Foi um total {dados["total"]} gols.')
print('>>>' * 5, ' Finalizado ', '<<<' * 5)



