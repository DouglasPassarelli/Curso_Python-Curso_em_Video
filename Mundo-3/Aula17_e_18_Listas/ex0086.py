'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[], [], []]
for c in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
print('-=' * 20)
for n in matriz:
    print(f'[{n[0]:^5}][{n[1]:^5}][{n[2]:^5}]')


