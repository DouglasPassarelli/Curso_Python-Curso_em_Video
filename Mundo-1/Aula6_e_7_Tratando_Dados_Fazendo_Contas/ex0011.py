# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de # tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²


largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
mq = largura * altura
tin = mq / 2
print('Sua parede tem o total de {}m²'.format(mq))
print('Sua dimensão e de {}x{}'.formta(largura, altura))
print('E necessario {:.1f} litros de tinta para pinta-la'.format(tin))
