'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  Ex:                                                                                                            

escreva(‘Olá, Mundo!’) 

Saída:                                                                                                                        ~~~~~~~~~                                                                                                      Olá, Mundo!
~~~~~~~~~

'''

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
