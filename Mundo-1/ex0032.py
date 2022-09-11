from datetime import date #modulo para saber saber a data
print('=' * 10, 'Ano Bissexto', '=' * 10)
ano = int(input('Em que ano estamos? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #Para saber o ano atual do computador
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {}, é um ano bissexto'.format(ano))
else:
    print('O ano de {} nao é um ano bissexto'.format(ano))
print('=' * 10, 'TERMINADO', '=' * 10)