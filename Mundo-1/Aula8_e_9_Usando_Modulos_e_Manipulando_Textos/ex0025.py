# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input('Digite seu nome:')).title().strip()
print('Exite Silva em {}'.format(nome))
print('Silva' in nome)
