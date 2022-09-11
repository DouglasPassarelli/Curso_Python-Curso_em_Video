frase = str(input('Digite um frase:')).strip()
print('Quantas vezes aparece a letra "A": {} vezes'.format(frase.lower().count('a')))
print('Em que posição a letra "A" aparece a primeira veiz? \nR:Aparece na posição {}'.format(frase.lower().find('a')+1))
print('Em que posição a letra "A" aparece a ultima veiz? \nR:Aparece na posição {}'.format(frase.lower().rfind('a')+1))
