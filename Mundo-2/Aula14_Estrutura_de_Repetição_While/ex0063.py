'''
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os primeiros n elementos e uma sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)
'''

print('-=' * 10, 'Sequencia de Fibonaci', '-=' * 10)
n = int(input('Digite a quantos termos de fibonaci deseja ver: '))
c = 3
ant = 0
if n >= 1:
    print('{} --> '.format(ant), end='')
suc = 1
if n >= 2:
    print('{} --> '.format(suc), end='')
while c <= n:
    soma = ant + suc
    print('{} --> '.format(soma), end='')
    ant = suc
    suc = soma
    c += 1
print('Finalizado', end='')
