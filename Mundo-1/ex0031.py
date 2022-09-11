print('=' * 10, 'Agencia de Viagens', '=' * 10)
distancia = float(input('Qual a distancia de sua viagem em Km:'))
if distancia <= 200:
    preço = distancia * 0.50
    print('Sua viagem ficou no valor de R$0.50 por Km')
    print('Sua viagem de {}Km, ficou no valor de R${:.2f}'.format(distancia, preço))
else:
    preço = distancia * 0.45
    print('Sua viagem ficou no valor de R$0.45 por km')
    print('Sua viagem de {}Km, ficou no valor de R${:.2f}'.format(distancia, preço))
print('Faça uma boa viagem!')

#Exemplo simplificado
#preço = diastancia * 0.50 if distancia <= 200 else distacia * 0.45

