'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import date
#aposenta com 35 anos de colaboração
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
anoatual = date.today().year
cadastro['idade'] = anoatual - nasc
cadastro['carteira de trabalho'] = int(input('Registro carteira de trabalho(0 igual a nao tem): '))
if cadastro['carteira de trabalho'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Qual o seu salario: R$ '))
    cadastro['aposentadoria'] = 35 - (anoatual - cadastro['contratação']) + cadastro['idade']
print('-=' * 35)
print('{:-^35}'.format(' Dados Cadastrados '))
for k, v in cadastro.items():
    print(f'>>> {k} tem o valor de {v} <<<')


