'''Aprimore o desafio anterior, mostrando no final:                                                    A) A soma de todos os valores pares digitados.                                                                                                  B) A soma dos valores da terceira coluna.                                                                                                       C) O maior valor da segunda linha.'''

matriz = [[], [], []]
soma = somat = maior = 0
for c in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
print('-=' * 20)
for n in matriz:
    print(f'[{n[0]:^5}][{n[1]:^5}][{n[2]:^5}]')
    somat += n[2]
    for m in matriz[1]:
        if m >= maior:
            maior = m
    for cont in n:
        if cont % 2 == 0:
            soma += cont
print('-=' * 20)
print(f'A soma de todos os valores pares da matriz é {soma}')
print(f'A soma dos valores da terceira coluna da matriz é {somat}')
print(f'O maior valor da segunda linha da matriz é {maior}')





