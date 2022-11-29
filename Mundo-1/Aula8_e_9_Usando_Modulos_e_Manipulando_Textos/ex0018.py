# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e 
# tangente desse ângulo.

import math
angulo = float(input('Digite o angulo: '))
coseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O seno do angulo {}º e {:.2f}'.format(angulo, seno))
print('O cosseno do angulo {}º e {:.2f}'.format(angulo, coseno))
print('A tangente do angulo {}º e {:.2f}'.format(angulo, tangente))

