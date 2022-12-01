'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
'''

print('-=' * 10, 'Calculo de IMC', '-=' * 10)
peso = float(input('Peso(kg): '))
altura = float(input('Altura(m): '))
sexo = str(input('Sexo: '))
imc = peso / altura ** 2
print('Sua altura e {:.2f} e seu peso e {:.2f}kg, calculando seu imc e {:.1f}'.format(altura, peso, imc))
if imc < 20.7:
    print('Voce esta ABAIXO DO PESO')
elif imc <= 25:
    print('Voce esta no PESO IDEAL')
elif imc <= 30:
    print('Voce esta com SOBREPESO')
elif imc <= 40:
    print('Voce esta com OBESIDADE')
elif imc > 40:
    print('Voce esta com OBESIDADE MORBIDA')


