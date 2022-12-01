''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''

quant = homem = mulher20 = 0
while True:
    sexo = r = ''
    print('=' * 35)
    print('       CADASTRE UMA PESSOA')
    print('=' * 35)
    idade = int(input('Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    print('=' * 35)
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        quant += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        if idade < 20:
            mulher20 += 1
    if r == 'N':
        break
print('=' * 40)
print(f'Tem no total {quant} pessoas maior de 18 anos cadastradas')
print(f'Tem ao todo um total de {homem} homens cadastrados')
print(f'Tem no total {mulher20} mulheres com menos de 20 anos cadastradas')
print('-=' * 10, 'LISTA DE CADASTRO FINALIZADO', '-=' * 10)