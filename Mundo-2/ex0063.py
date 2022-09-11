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

'''a = 0
b = 1
d = 0
print('{} --> '.format(a), end='')
print('{} --> '.format(b), end='')
for c in range(3, 15+1):
    d = a + b
    print('{} --> '.format(d), end='')
    a = b
    b = d'''
