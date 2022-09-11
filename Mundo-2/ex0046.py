import emoji
from time import sleep
print('-=' * 10, 'Contagem regressiva', '-=' * 10)
print('Contagem regressiva para os fogos de artificio')
for contagem in range(10, 0-1, -1):
    sleep(1)
    print(contagem)
print(emoji.emojize('\U0001f387 \u2728 \U0001f389' * 10))
print('\033[4;31mFELIZ ANO NOVOOOOO')
print(emoji.emojize('\U0001f387 \u2728 \U0001f389' * 10))
