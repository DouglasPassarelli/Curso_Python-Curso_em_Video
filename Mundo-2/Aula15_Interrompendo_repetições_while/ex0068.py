''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou, 
no final do jogo.'''

from random import randint
print('-=' * 10, 'Jogo Par ou Impar', '-=' * 10)
computador = randint(0, 10)
soma = quant = 0
resultado = ''
while True:
    n = int(input('Digite um numero: '))
    parimpar = str(input('Escolha Par ou Impar: [P ou I]: ')).upper().strip()[0]
    if parimpar != 'P' and parimpar != 'I':
        print('Resposta Invalida! Tente novamente')
    else:
        print('=' * 30)
        soma = n + computador
        if soma % 2 == 0:
            resultado = 'Par'
        else:
            resultado = 'Impar'
        print(f'Voce jogou {n} e o computador jogou {computador}. Total deu {soma} Deu {resultado}')
        print('-=-' * 10)
        if resultado[0] == parimpar:
            print('Voce venceu!')
            print('Vamor jogar novamente...')
            print('=' * 30)
            quant += 1
        else:
            print('Voce PERDEU!')
            print('=' * 30)
            break
print(f'Game Over! Voce venceu {quant} vezes.')








