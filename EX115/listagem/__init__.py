def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um numero Inteiro valido!!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuario preferiu nao digitar esse valor.\033[m')
            return 0
        else:
            return n


def linhas(tam=42):
    print('-' * tam)


def cabecalho(msg):
    linhas()
    print(msg.center(42))
    linhas()

def menu(lista):
    cabecalho(' MENU PRINCIPAL ')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    linhas()
    opcao = leiaint('\033[33mSua opção: \033[m')
    return opcao




def cadastradas(pes):
    cabecalho(' PESSOAS CADASTRADAS ')
    if len(pes) == 0:
        print('Ainda nao foram cadastradas nenhuma pessoa!')


def nova(pes):
    cabecalho(' NOVO CADASTRO ')
    p = {}
    p['Nome'] = str(input('Nome: '))
    p['Idade'] = int(input('Idade: '))
    print(f'Registro de {p["Nome"]} foi adicionado com sucesso.')
    pes.append(p.copy())

