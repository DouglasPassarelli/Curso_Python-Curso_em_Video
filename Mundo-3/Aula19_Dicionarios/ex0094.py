'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
'''

cadastro = []
soma = 0
#FORNECENDO OS DADOS
while True:
    r = ' '
    pessoas = {}
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F]: '))
    while pessoas['sexo'] not in 'MmFf':
        print('ERRO! Por favor digite apenas M ou F')
        pessoas['sexo'] = str(input('Sexo: [M/F]: '))
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    cadastro.append(pessoas.copy())
    r = str(input('Quer continuar ?[S/N]: ')).strip()[0]
    while r not in 'NnSs':
        print('Erro! Por favor, digite apenas S ou N')
        r = str(input('Quer continuar ?[S/N]: ')).strip()[0]
    if r in 'nN':
        break
# ANALISE DE DADOS
media = soma / len(cadastro)
print('-=' * 30)
print(f'>>> Foram cadastradas um total de {len(cadastro)} pessoas.')
print(f'>>> A media de idade do grupo é {media} anos')
print('>>> As mulheres cadastradas foram: ', end='')
for c in cadastro:
    if c['sexo'] in 'Ff':
        print(c['nome'], end=' ')
print('\n>>> Listas das pessoas que estão acima da media: ')
print()
for c in cadastro:
    if c['idade'] > media:
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
        print()
print('{:=^30}'.format(' FINALIZADO '))

