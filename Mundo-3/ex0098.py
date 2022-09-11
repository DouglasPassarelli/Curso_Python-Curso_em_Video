'''from time import sleep
def contagem(inicio, fim, passo):
    print('-=' * 20)
    print('Contagem de 1 ate 10 pulando de 1 em 1.')
    for c in range(1, 11):
        print(c, end=' ')
    print('Fim!')
        #sleep(0.5)
    print('-=' * 20)
    print('Contagem de 10 ate 0 pulando de 2 em 2.')
    for c in range(10, -1, -2):
        print(c, end=' ')
    print('Fim!')
    print('-=' * 20)
    print('Agora sua veiz de personalizar a contagem!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('-=' * 20)
    print(f'Contagem de {inicio} ate {fim} pulando de {passo} em {passo} ')
    if inicio >= fim and passo > 0:
        soma = passo + passo
        passo = passo - soma
        fim -= 1
    if passo < 0:
        fim -= 1
    if passo == 0:
        if fim > 0:
            passo += 1
            fim += 1
        else:
            passo -= 1
            fim -= 1
    for c in range(inicio, fim, passo):
        print(c, end=' ')
    print('Fim!')
    print('-=' * 20)


contagem(0, 10, 1)'''

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