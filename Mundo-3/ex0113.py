def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um numero Real valido!!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuario preferiu nao digitar esse valor.\033[m')
            return 0
        else:
            return n





def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um numero Real valido!!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuario preferiu nao digitar esse valor.\033[m')
            return 0
        else:
            return n




#progama principal
i = leiaint('Digite um inteiro: ')
r = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o valor real digitado foi {r} ')
