''' Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade = float(input('Quantos Km/h o carro estava?'))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Voce foi multado por excesso de velocidade!')
    print('Excedeu o limite de velocidade de 80km/h')
    print('Voce estava a {}Km/h ,Sua multa vai ser de R${:.2f}'.format(velocidade, multa))
print('Voce esta dentro do limite de velocidade! Parabens')