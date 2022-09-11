n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero:'))
cores = {'azul': '\033[34m', 'limpa': '\033[m', 'roxo': '\033[35m'}
s = n1 + n2
print('\033[4;31mA soma de {}{}{} \033[4;31me {}{}{} \033[4;31me igual a {}{}'.format(cores['azul'], n1, cores['limpa'], cores['azul'], n2, cores['limpa'], cores['roxo'], s, cores['limpa']))
