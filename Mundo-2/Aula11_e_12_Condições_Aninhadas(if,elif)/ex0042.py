'''
Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''

print('-=' * 15, 'Analisando Triangulos', '-=' * 15)
reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))
print('Com as retas {}, {} e {}'.format(reta1, reta2, reta3))
if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta1 + reta2:
    print('Pode-se formar um TRIANGULO ')
    if reta1 == reta2 and reta2 == reta3: #outra forma de fazer e (reta1 == reta2 == reta3)
        print('O triangulo é Equilátero')
    elif reta1 == reta2 and reta2 != reta3 or reta3 == reta2 and reta1 != reta2 or reta3 == reta1 and reta2 != reta1:
        print('O triangulo é Isósceles')
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1: #outra forma de fazer e (reta1 != reta2 != reta3
        print('O triangulo é Escaleno')
else:
 print('Não pode formar um TRIANGULO')
print('-=' * 20, 'TERMINADO', '-=' * 20)

