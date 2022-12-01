'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares
Se o valor digitado for ímpar, desconsidere-o.'''

print('-=' * 10, 'Soma dos Pares', '-=' * 10)
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('digite o {}° numero: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Ao todos foram {} numero pares'.format(cont))
print('A soma dos numeros pares é {}'.format(soma))
