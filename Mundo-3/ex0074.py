from random import randint
cont = maior = menor = 0
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Listagem de numeros: {num}')
for c in num:
    cont += 1
    if cont == 1:
        maior = c
        menor = c
    if c >= maior:
        maior = c
    if c <= menor:
        menor = c
print(f'O maior numero da listagem foi: {maior}')
print(f'O menor numero da listagem foi: {menor}')


