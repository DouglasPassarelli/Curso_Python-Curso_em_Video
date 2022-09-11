def ficha(n, g):
    if n == '':
        n = '<desconhecido>'
    if g == '' or g.isalpha():
        g = 0

    return f'O jogador {n} fez {g} gols no campeonato'

print('-' * 20)
nome = str(input('Nome do Jogador: '))
gols = str(input('Numero de Gols: '))
print(ficha(nome, gols))




