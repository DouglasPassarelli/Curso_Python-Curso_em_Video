''' Crie um programa que leia uma frase qualquer
E diga se ela é um palíndromo, desconsiderando os espaços'''
# Após a sopa
# A sacada da casa
# A torre da derrota
# o lobo ama o bolo
# Anotaram a data da maratona


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






