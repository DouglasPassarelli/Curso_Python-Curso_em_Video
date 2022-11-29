# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# Ex.: Ana Maria de Souza
# Primeiro = Ana
# Último: Souza

nome = str(input('Digite seu nome completo:')).strip()
nome1 = nome.split()
print('Muito prazer em te conhecer {}'.format(nome))
print('Primeiro nome:{}'.format(nome1[0]))
print('Ultimo nome:{}'.format(nome1[-1])) #Segunda opçao (nome1[len(nome1)-1]
