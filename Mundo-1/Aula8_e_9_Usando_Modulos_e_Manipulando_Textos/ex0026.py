# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite um frase:')).strip()
print('Quantas vezes aparece a letra "A": {} vezes'.format(frase.lower().count('a')))
print('Em que posição a letra "A" aparece a primeira veiz? \nR:Aparece na posição {}'.format(frase.lower().find('a')+1))
print('Em que posição a letra "A" aparece a ultima veiz? \nR:Aparece na posição {}'.format(frase.lower().rfind('a')+1))
