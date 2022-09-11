from time import sleep
from random import randint #Fazer um randonização de um numero
print('\033[1;31m{:=^55}' .format(' Jogo Pedra, Papel, Tesoura '))
lista = ('pedra', 'papel', 'tesoura') #Colocar as strings em uma lista
computador = randint(0, 2) #Fazer o computador sortear um numero de 0 a 2
print('\033[4;34mTente vencer o computador!')
print('''O que deseja jogar ?
[0] para Pedra
[1] para Papel
[2] para Tesoura ''')
escolha = int(input('Sua opção: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-=' * 15)
print('\033[32mO computador jogou {}'.format(lista[computador]))#Fazer o sortei dos elementos da lista
print('O jogador jogou {}\033[m'.format(lista[escolha]))#Fazer com que a opção selecionada seja o mesmo numero referente ao da lista
print('\033[34m-=\033[m' * 15)
if computador == 0: #jogada do computador
    if escolha == 0: #comparando com a jogada do jogador
        print('\033[33mTemos um empate!')
    elif escolha == 1:
        print('\033[32mO Jogador venceu!')
    elif escolha == 2:
        print('\033[32mO Computador venceu!')
    else:
        print('\033[31mJogada Invalida!')
elif computador == 1:
    if escolha == 0:
        print('\033[32mO Computador venceu!')
    elif escolha == 1:
        print('\033[33mTemos um empate!')
    elif escolha == 2:
        print('\033[32mO Jogador venceu!')
    else:
        print('\033[31mJogada Invalida')
elif computador == 2:
    if escolha == 0:
        print('\033[32mO Jogador Venceu!')
    elif escolha == 1:
        print('\033[32mO Computador Venceu!')
    elif escolha == 2:
        print('\033[33mTemos um empate!')
    else:
        print('\033[4;31mOpção invalida, Tente novamente!')
print('\033[34m{:=^30}' .format(' TERMINADO '))

#fazer uma condição aninhada para fazer os testes se o computador venceu ou se o jogador venceu!!!

