def area(a, b):
    s = a * b
    print(f'A area do terreno com  {a} X {b}mts quadrados e de {s:.1f}m²')

#Progama Principal
print(' Controle de Terrenos ')
print('-' * 30)
largura = float(input('Largura(m): '))
comprimento = float(input('Comprimento(m): '))

area(a=largura, b=comprimento)
