def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um numero inteiro valido!!!\033[m')
        if ok:
            break
    return valor

def leiadinheiro(msg):
    n = ''
    while True:
        n = str(input(msg)).strip()
        if n.isalpha() or n == '':
            print(f'\033[31mERRO! "{n}" é um preço invalido\033[m')
        else:
            num = []
            num = n
            for c in num:
                if c == '.':
                    return float(n)
                if c == ',':
                    n = n.replace(',', '.')
                    return float(n)
            return float(n)
            print(f'\033[31mERRO! "{n.strip()}" é um preço invalido\033[m')


