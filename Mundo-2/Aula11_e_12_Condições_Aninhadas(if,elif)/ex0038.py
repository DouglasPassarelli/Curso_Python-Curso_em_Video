'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior; os dois são iguais
'''


primeiro = int(input('Digite um numero: '))
segundo = int(input('Digite um outro numero: '))
print('Comparando os valores de {} e {}'.format(primeiro, segundo))
if primeiro > segundo:
    print('O \033[34mprimeiro\033[m valor e \033[34mMAIOR')
elif segundo > primeiro:
    print('O \033[34msegundo\033[m valor e \033[34mMAIOR')
elif primeiro == segundo:
    print('\033[31mNão existe valor maior os dois sao iguais')
print('\033[34m=' * 20, 'Terminado', '=' * 20)
