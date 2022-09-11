nome = str(input('Digite seu nome completo:')).strip()
nome1 = nome.split()
print('Muito prazer em te conhecer {}'.format(nome))
print('Primeiro nome:{}'.format(nome1[0]))
print('Ultimo nome:{}'.format(nome1[-1])) #Segunda opçao (nome1[len(nome1)-1]
