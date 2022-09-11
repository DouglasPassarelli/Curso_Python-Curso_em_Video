'''print('-=' * 10, 'Analisando Frases', '-=' * 10)
frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
frase2 = str(frase[::-1])
frase2 = frase2.replace(' ', '')
if frase == frase2:
    print('A frase {} ao inverso fica {} e é um PALINDROMO!!'.format(frase, frase2))
else:
    print('A frase {} ao inverso fica {} e nao é um PALINDROMO!!'.format(frase, frase2))'''

frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = '' #adicionar o valor da string 
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]

if junto == inverso:
    print('A frase {} ao contrario fica {} e é um PALINDROMO!!'.format(junto, inverso))
else:
    print('A frase {} ao contrario fica {} e nao é um PALINDROMO!!'.format(junto, inverso))






