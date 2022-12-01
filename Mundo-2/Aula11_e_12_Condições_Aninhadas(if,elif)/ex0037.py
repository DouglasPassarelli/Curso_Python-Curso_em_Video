''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal
'''


num = int(input('\033[4;31mDigite um numero: '))
print('\033[31mDigite qual base quer fazer a conversão')
resp = str(input('\033[31m[1] para binario\n[2] para octal\n[3] para hexadecimal\nSua Opção:'))
lista = ['1', '2', '3']
if resp == (lista[0]):
    print('\033[36mO numero {} em binario ficará {}'.format(num, format(num, 'b')))  #Função bin() achara o binario, a função format(value, 'b') retorna o numero binario sem o prefixo
elif resp == (lista[1]):
    print('\033[36mO numero {} em octal ficará {}'.format(num, format(num, 'o')))#A função oct() retorna o valor em octal, a funçao format(value, 'o') retorna o numero em octal sem o prefixo
elif resp == (lista[2]):
    print('\033[36mO numero {} em hexadecimal ficará {}'.format(num, format(num, 'x')))#A função hex() retorna o valor em hexadecimal, a funçao format(value, 'x') retorna o numero em hexadecimal sem o prefixo
else:
    print('Opção invalida, tente novamente')
