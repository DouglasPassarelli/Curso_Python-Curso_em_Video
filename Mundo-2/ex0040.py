from math import ceil
n1 = float(input('\033[37mPrimeira nota: '))
n2 = float(input('\033[37mSegunda nota: '))
media = (n1 + n2) / 2
print('\033[34mSua primeira nota foi de {:.1f} e sua segunda nota foi de {:.1f}, sua media ficou em {:.1f}'.format(n1, n2, media))
if media < 5:
    print('\033[31mVoce esta REPROVADO!')
    print('\033[31mVoce ficou abaixo da media')
elif media >= 5 and media <= 6.9:
    print('\033[33mVoce esta em RECUPERAÇÃO')
elif media >= 7:
    print('\033[32mParabens! Voce foi APROVADO')
print('\033[37m-=' * 15, 'TERMINADO', '-=' * 15)

