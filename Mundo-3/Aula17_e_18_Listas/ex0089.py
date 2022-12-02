'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

pessoas = []
temp = list()
while True:
    temp = []
    r = ''
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    temp.append(nome)
    temp.append(media)
    temp.append([n1, n2])
    pessoas.append(temp[:])
    r = str(input('Quer continuar ?[S/N]: '))
    if r in 'Nn':
        break
print('-=' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 40)
for i, c in enumerate(pessoas):
    print(f'{i:<4}{c[0]:<10}{c[1]:>8.1f}')
print('-' * 40)
while True:
    notas = int(input('Mostrar notas de qual aluno ?(999 para interromper)'))
    print('-' * 40)
    for i, c in enumerate(pessoas):
        if notas == i:
            print(f'As notas de {c[0]} sao: {c[2]}')
            print('-' * 40)
    if notas == 999:
        break
print('>>>' * 5, 'Finalizado', '<<<' * 5)







