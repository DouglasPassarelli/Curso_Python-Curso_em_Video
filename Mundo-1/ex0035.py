'''#Feito por min
print('-=' * 25)
print(' ' * 13, 'Analisador de Triangulos')
print('-=' * 25)
r1 = float(input('Qual o comprimento da primeira reta:'))
r2 = float(input('Qual o comprimento da segunda reta:'))
r3 = float(input('Qual o comprimento da terceira reta:'))
#Localizando o primeiro lado menor
menorl1 = r1
if r2 < r1 and r2 < r3:
    menorl1 = r2
if r3 < r1 and r3 < r2:
    menorl1 = r3
#Localizando o segundo lado menor
maiorlado = r1
if r2 > r1 and r2 > r3:
    maiorlado = r2
if r3 > r1 and r3 > r2:
    maiorlado = r3
#Achando o valor da terceira reta
if r1 != maiorlado and r1 != menorl1:
    lado3 = r1
if r2 != maiorlado and r2 != menorl1:
    lado3 = r2
if r3 != maiorlado and r3 != menorl1:
    lado3 = r3
if (lado3 + menorl1) > maiorlado:
    print('Pode formar um triangulo!')
else:
    print('Não pode formar um triangulo!')'''

#Forma simplificada

print('-=' * 20)
print(' ' * 10, 'Analisador de Triangulo')
print('-=' * 20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo!')
else:
    print('Os segmentos acima NAO PODEM FORMAR um triangulo!')
print('-=' * 10, 'Terminado', '-=' * 10)





