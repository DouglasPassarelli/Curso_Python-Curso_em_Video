'''valores = list()
for c in range(0, 5):
    valor = int(input('Digite um valor:'))
    if c == 0:
        valores.append(valor)
        print('Valor adicionado no final da lista')
    if c == 1:
        if valores[0] > valor:
            valores.insert(0, valor)
            print('Valor adicionado na posição 0')
        else:
            valores.append(valor)
            print('Valor adicionado no final da lista')
    if c == 2:
        if valor < valores[0]:
            valores.insert(0, valor)
            print('Valor adicionado na posição 0')
        elif valores[0] < valor and valores[1] > valor:
            valores.insert(1, valor)
            print('Valor inserido na posição 1')
        elif valor > valores[0] and valor > valores[1]:
            valores.append(valor)
            print('Valor adicionado no final da lista')
    if c == 3:
        if valor < valores[0]:
            valores.inser(0, valor)
            print('Valor adicionado na posição 0')
        elif valor > valores[0] and valor < valores[1]:
            valores.insert(1, valor)
            print('Valor adicionado na posição 1')
        elif valor > valores[1] and valor < valores[2]:
            valores.insert(2, valor)
            print('Valor adicionado na posição 2')
        elif valor > valores[2]:
            valores.append(valor)
            print('Valor adicionado no final da lista')
    if c == 4:
        if valor < valores[0]:
            valores.insert(0, valor)
            print('Valor adicionado na posição 0')
        elif valor > valores[0] and valor < valores[1]:
            valores.insert(1, valor)
            print('Valor adicionado na posição 1')
        elif valor > valores[1] and valor < valores[2]:
            valores.insert(2, valor)
            print('Valor adicionado na posição 2')
        elif valor > valores[2] and valor < valores[3]:
            valores.insert(3, valor)
            print('Valor adicinonado na posição 3')
        elif valor > valores[3]:
            valores.append(valor)
            print('Valor adicionado no final da lista')
print('-=' * 35)
print(f'Lista: {valores}')'''

#MELHORAR O RACIOCIO LOGICO PARA NAO FAZER CODIGOS TAO GRANDES

#Codigo do guanabara

valores = list()
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                print(f'O Valor foi adicionado na posição {pos}')
                break
            pos += 1
print(f'Lista: {valores}')
