preço = float(input('Qual o preço do produto ? R$'))
desconto = preço * 5 / 100
novopreço = preço - desconto
print('O produto na liquidação com 5% de desconto, fica de R${:.2f} para R${:.2f}'.format(preço, novopreço))
