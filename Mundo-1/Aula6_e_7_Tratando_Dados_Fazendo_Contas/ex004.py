# Faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre ele


entrada = input('Digite algo:')
print('O tipo primitivo desse valor é', type(entrada))
print('Só tem espaços ?', entrada.isspace())
print('É um numero?', entrada.isnumeric())
print('É alfabetico?', entrada.isalpha())
print('É alfanumerico?', entrada.isalnum())
print('Está em maiscúlas?', entrada.isupper())
print('Está em minúsculas?', entrada.islower())
print('Está capitalizada?', entrada.istitle())
