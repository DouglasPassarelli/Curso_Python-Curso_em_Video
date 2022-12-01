'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''

from datetime import date


print('\033[4;36m-=' * 15, 'ALISTAMENTO MILITAR', '-=' * 15)
nasc = int(input('\033[31mEm que ano voce nasceu: '))
sexo = str(input(' Qual o seu sexo ? (masculino) ou (feminino) '))
lista = ['feminino', 'masculino']
ano = date.today().year
idade = ano - nasc
if sexo == (lista[0]):
    print('Lamentamos mais apenas pessoas do sexo MASCUILINOS podem se alistar!')
if idade < 18 and sexo == lista[1]:
    saldo = 18 - idade
    atual = ano + saldo
    print('\033[31mVoce ainda vai se alistar')
    print('\033[31mSua idade e de {}'.format(idade))
    print('\033[31mFalta {} anos para voce se alistar!'.format(saldo))
    print('\033[31mSeu alistamento sera no ano de {}'.format(atual))
elif idade == 18 and sexo == lista[1]:
    print('\033[32mVoce completou {} anos'.format(idade))
    print('\033[32mJa e a hora de se alistar!')
elif idade > 18 and sexo == lista[1]:
    saldo = idade - 18
    atual = ano - saldo
    print('\033[33mJá passou da hora de se alistar!')
    print('Voce tem {} anos, e passou {} anos do prazo do alistamento militar'.format(idade, saldo))
    print('Seu alistamento foi em {}'.format(atual))
print('\033[4;36m-=' * 15, 'TERMINADO', '-=' * 15)