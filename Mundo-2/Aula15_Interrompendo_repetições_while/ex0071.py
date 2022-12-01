'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado(inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''


'''print('-=' * 15)
print('{:^30}'.format('BANCO DO DOGAO'))
print('-=' * 15)
cedulas = (50, 20, 10, 1)
valor = int(input('Qual valor deseja sacar: R$'))
for cedula in cedulas:
    quantcedula = valor // cedula
    valor = valor - quantcedula * cedula
    print(f'Total de {quantcedula} de cédulas de R${cedula:.2f}')
print('-=' * 15)
print('VOLTE SEMPRE BANCO DO DOGAO AGRADEÇE SUA PRESENÇA!!')'''


#Segundo Metodo


print('-=' * 15)
print('{:^30}'.format('BANCO DO DOGAO'))
print('-=' * 15)
valor = int(input('Digite o valor que queira sacer: R$ '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} de cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('{:=^50}'.format(' Finalizado '))
print('Banco do Dogão agredece sua presença volte sempre!!!')
