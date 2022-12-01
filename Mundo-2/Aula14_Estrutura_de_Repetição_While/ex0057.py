'''
Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''

resp = str(input('Informe seu Sexo: [M/F] ')).upper().strip()[0]
while resp != 'M' and resp != 'F':
    resp = str(input('Dados Invalidos! Por favor, Informe seu Sexo novamente: ')).upper().strip()[0]
if resp == 'M':
    print('Sexo M cadastrado com sucesso!')
else:
    print('Sexo F cadastrado com sucesso!')


