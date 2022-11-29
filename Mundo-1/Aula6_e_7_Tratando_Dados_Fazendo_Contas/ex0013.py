# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Qual o seu salario ? R$'))
nsalario = salario + (salario * 15 / 100)
print('Seu salario atual e de R${:.2f}, e com o almento de 15 % ficara R${:.2f}'.format(salario, nsalario))
