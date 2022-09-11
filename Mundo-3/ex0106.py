from time import sleep
c = ('\033[m',   # 0 sem cor
       '\033[4;30;44m',   # 1 branco e azul
       '\033[4;31;45m',   # 2 vermelho e roxo
       '\033[4;33;42m',   # 3 amarelo e verde
       '\033[4;36;47m')          # 4 azul marinho e cinza


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')



def ajuda(resp):
    titulo(f"BUSCANDO A BIBLIOTECA '{resp}' ", 3)
    sleep(2)
    print(c[1], end='')
    help(resp)


#Progama principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO')




