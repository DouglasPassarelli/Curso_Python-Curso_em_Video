''' 
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

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




