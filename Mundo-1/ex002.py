#Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado

nome = input('\033[4;37mQual seu nome ? ')
print('Muito prazer em te conhecer, {}{}{}!' .format('\033[33m', nome, '\033[m'))

