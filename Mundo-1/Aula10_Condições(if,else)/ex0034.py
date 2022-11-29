'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de R$ 15%.
'''

print('=' * 20, 'Aumento Salarial', '=' * 20)
salario = float(input('Qual o salario do funcionario ? R$'))
aumento1 = salario * 10 / 100
aumento2 = salario * 15 / 100
if salario >= 1250:
    nsalario = salario + aumento1
else:
   nsalario = salario + aumento2
print('O funcionario com o salario de  R${:.2f}, com o aumento passa a receber R${:.2f}'.format(salario, nsalario))
print('=' * 35, 'Terminado', '=' * 35)

