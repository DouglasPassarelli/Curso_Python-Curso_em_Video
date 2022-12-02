'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final
mostre:                                                                                                    
A) Quantas pessoas foram cadastradas.                                                                                                   B) Uma listagem com as pessoas mais
pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.'''

listagem = list()
dados = list()
cadastro = maior = cont = menor = 0
while True:
    r = ' '
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso(kg): ')))
    cadastro += 1
    listagem.append(dados[:])
    dados.clear()
    for p in listagem:
        if cont == 0:
            menor = p[1]
        cont += 1
        if p[1] >= maior:
            maior = p[1]
        if p[1] <= menor:
            menor = p[1]
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 20)
print(f'Foram cadastrados {cadastro} pessoas!')
print(f'O maior peso foi de {maior}KG, e a pessoa mais pesada foi ', end='')
for p in listagem:
    if p[1] == maior:
        print(p[0], end=' ')

print(f'\nA pessoa mais leve pesa {menor}Kg, e a pessoa mais leve foi ', end='')
for p in listagem:
    if p[1] == menor:
        print(p[0], end=' ')




#Resolução do Gustavo guanabara
'''temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso(Kg):')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input('Quer continuar ? [S/N]: '))
    if r in 'Nn':
        break
print('-=' * 20)
print(f'Foram cadastradas {len(princ)} pessoas!')
print(f'O maior peso foi de {mai}. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()'''


