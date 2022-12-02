''' 
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

from datetime import date
def voto(nasc):
    ano = date.today().year
    idade = ano - nasc
    print(f'Com {idade} anos: ', end='')
    if idade >= 18 and idade <= 70:
        return 'VOTO OBRIGATORIO.'
    if idade < 16:
        return 'NAO VOTA.'
    if idade >= 70 or idade >= 16 and idade < 18:
        return 'VOTO OPCIONAL.'


print('-=' * 20)
ano = int(input('Em que ano voce nasceu ? '))
print(voto(ano))
