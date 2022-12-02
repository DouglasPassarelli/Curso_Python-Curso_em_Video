'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(n, show=False):
    """
    --> Calculo fatorial de um numero>
    :param n:O numero a ser calculado
    :param show:(opcional) se deseja mostrar ou nao com a conta
    :return:O valor da Factorial de n
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
