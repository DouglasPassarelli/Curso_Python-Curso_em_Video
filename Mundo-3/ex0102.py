def fatorial(n, show=False):
    """
    --> Calculo fatorial de um numero>
    :param n:O numero a ser calculado
    :param show:(opcional) se deseja mostrar ou nao com a conta
    :return:O valo da Factorial de n
    """
    print('--' * 30)
    f = 1
    for c in range(n, 1 - 1, -1):
        f *= c
        if show:
            print(c, end='')
            print(' x ' if c > 1 else ' = ', end='')
    return f


print(fatorial(5, show=True))
#help(fatorial)
