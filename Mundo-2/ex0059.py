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


#Codigo do guanabara
#from time import sleep
#n1 = int(input('Primeiro valor: '))
#n2 = int(input('Segundo valor: '))
#opcao = 0
#while opcao != 5
    #print('''    [1] Somar
    #[2] Multiplicar
    #[3] Maior
    #[4] Novos numeros
    #[5] Sair do progama''')
    #opcao = int(input((' >>>> Qual e a sua Opção? ')))
    #if opcao == 1:
        #soma = n1 + n2
        #print('A soma entre {} + {} é {}'.format(n1, n2, soma))
#elif opcao == 2:
        #produto = n1 * n2
        #print('O resultado entre {} x {} é {}'.format(n1, n2, produto))
#elif opcao == 3:
        #if n1 > n2:
# maior = n1
        #else:
            #maior = n2
        #print('Entre a opção {} e {} o maior valor e {}'.format(n1, n2, maior))
#elif opcao == 4:
        #print('Informe os numero novamente:')
        #n1 = int(input('Digite um numero: '))
        #n2 = int(input('Digite outro numero: '))
#elif opcao == 5:
        #print('Finalizando')
#else:
        #print('Opção Invalida. Tente Novemente')
    #print('=-=' * 10)
    #sleep(2)
#print('Final do Progama! Volte sempre!')

