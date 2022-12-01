''' Crie um programa que leia dois valores e mostre um menu
na tela:
1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa
Seu programa deverá realizar a operação solicitada em cada caso '''

r = 0
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
while r != 5:
    print('''Menu de Opções
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do progama''')
    r = int(input('Qual opção deseja: '))
    print('-=' * 20)
    if r == 1:
        soma = n1 + n2
        print('A soma do numero {} com o numero {} é igual a {}'.format(n1, n2, soma))
        print('-=' * 10, 'Finalizado', '-=' * 10)
    elif r == 2:
        mult = n1 * n2
        print('A multiplicação do numero {} com o numero {} é igual a {}'.format(n1, n2, mult))
        print('-=' * 10, 'Finalizado', '-=' * 10)
    elif r == 3:
        if n1 > n2:
            print('Entre o numero {} e o numero {} o numero {} e o MAIOR'.format(n1, n2, n1))
            print('-=' * 10, 'Finalizado', '-=' * 10)
        else:
            print('Entre o numero {} e o numero {} o numero {} e o MAIOR'.format(n1, n2, n2))
            print('-=' * 10, 'Finalizado', '-=' * 10)
    elif r == 4:
        n1 = int(input('Digite um novo numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print('-=' * 20)
    else:
        if r != 5:
            print('Opção invalida! Tente Novamente')
            print('-=' * 20)
print('-=' * 10, 'Progama Encerrado', '-=' * 10)
