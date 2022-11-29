# Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.


nome = str(input('Digite seu nome:')).strip() #remove os espaços inuteis
nomes = len(nome.replace(' ', ''))  #ou len(nome) - nome.count(' ') ( le o nome e subtrai os espaços)
nomesp = (nome.split())  #ou nome.find(' ') (conta ate chegar no primeiro espaço)
print('{} com todas as letras maiusculas ficara:{}'.format(nome, nome.upper()))
print('{} com todas as letras minusculas ficara:{}'.format(nome, nome.lower()))
print('Quantas letras {} tem ao todo(sem considerar os espaços):{} letras'.format(nome, nomes))
print('Seu primeiro nome e {},e ele tem {} letras'.format(nomesp[0], len(nomesp[0])))


