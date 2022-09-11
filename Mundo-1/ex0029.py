velocidade = float(input('Quantos Km/h o carro estava?'))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Voce foi multado por excesso de velocidade!')
    print('Excedeu o limite de velocidade de 80km/h')
    print('Voce estava a {}Km/h ,Sua multa vai ser de R${:.2f}'.format(velocidade, multa))
print('Voce esta dentro do limite de velocidade! Parabens')