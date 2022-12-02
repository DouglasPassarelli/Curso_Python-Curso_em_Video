'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                                        

a) de 1 até 10, de 1 em 1  
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''


from time import sleep
def contagem(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        print('-=' * 20)
        print(f'Contamgem de {i} ate {f} pulando de {p} em {p}!')
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.5)
        print('Fim!')
    else:
        print(f'Contagem de {i} ate {f} pulando de {p} em {p}!')
        for c in range(i, f - 1, -p):
            print(c, end=' ')
            sleep(0.5)
        print('Fim!')
    print('-=' * 20)


contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora sua veiz de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)