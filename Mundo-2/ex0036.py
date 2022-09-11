print('\033[31m=' * 61)
print('\033[36m=' * 20, '\033[36mEmprestimo Báncario', '\033[36m=' * 20)
print('\033[31m=' * 61)
valorcasa = float(input('\033[36mDigite o valor da casa que queira comprar: R$'))
salario = float(input('Digite seu salario: R$'))
ano = int(input('Em quantos anos pretende pagar a casa ?\033[m'))
print('\033[34m-=' * 40)
salario1 = salario * 30 / 100
parcela = (valorcasa / ano) / 12
print('Voce pagara em {} anos, com o valor de cada prestação mensal um valor de  R${:.2f}'.format(ano, parcela))
print('Até o valor da casa que e R${:.2f}'.format(valorcasa))
print('\033[34m-=' * 40)
if parcela > salario1:
    print('\033[31mLamentamos muito, mais seu emprestimo foi negado!')
    print('\033[31mPois excedeu o valor de 30% do salario')
else:
    print('\033[35mParabens! Seu emprestimo foi aprovado e voce consiguira comprar sua casa')
    print('\033[35mA casa ficou no valor de R${:.2f}, em {} anos, com o valor da parcela em R${:.2f}'.format(valorcasa, ano, parcela))
print('\033[34m=' * 35, 'Terminado', '=' * 35)
