def moeda(n=0, nota='R$'):
    return f'{nota}{n:.2f}'.replace('.', ',')


def metade(n=0, show=False):
    num = n / 2
    if show:
        return moeda(num)
    return num


def dobro(n=0, show=False):
    num = n * 2
    if show:
        return moeda(num)
    return num

def aumentar(n=0, por=0, show=False):
    num = n + (n * por / 100)
    if show:
        return moeda(num)
    return num


def diminuir(n=0, por=0, show=False):
    num = n - (n * por / 100)
    if show:
        return moeda(num)
    return num


def resumo(n, por=0, pon=0):
    print('~' * 30)
    print('{:^30}'.format(' RESUMO DO VALOR '))
    print('~' * 30)
    print(f'{"Preço analisado"}: \t{moeda(n)}')
    print(f'{"Dobro do preço"}:  \t{dobro(n, True)}')
    print(f'{"Metade do preço"}: \t{metade(n, True)}')
    print(f'{por}% de aumento: \t{aumentar(n, por, True)}')
    print(f'{pon}% de redução: \t{diminuir(n, pon, True)}')
    print('~' * 30)