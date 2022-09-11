def escreva(txt):
    pos = 0
    while pos < len(txt):
        print('~', end='')
        pos += 1
    print(f'\n{txt}')
    pos = 0
    while pos < len(txt):
        print('~', end='')
        pos += 1
    print()


#Progama Principal
escreva(' Ola Mundo ')
escreva(' Curso em Video Python ')
escreva(' Gustavo Guanabara ')
escreva(' CeV ')
