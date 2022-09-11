from datetime import date
print('\033[31m-=' * 10, 'Confederação Nacional de Natação', '-=' * 10)
nasc = int(input('Em que ano voce nasceu: '))
atual = date.today().year
idade = atual - nasc
print('Voce nasceu no ano de {} e tem {} anos'.format(nasc, idade))
if idade <= 9:
    print('\033[32mCategoria:Mirim\033[m')
elif idade <= 14:
    print('\033[32mCategoria:Infantil\033[m')
elif idade <= 19:
    print('\033[32mCategoria:Junior\033[m')
elif idade <= 25:
    print('\033[32mCategoria:Sênior\033[m')
elif idade > 25:
    print('\033[32mCategoria:MASTER\033[m')
print('\033[31mNa Confederação Nacional de Natação')
print('-=' * 10, 'TERMINADO', '-=' * 10)

