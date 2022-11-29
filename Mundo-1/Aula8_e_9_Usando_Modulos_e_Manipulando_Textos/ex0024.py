# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"

#cidade = str(input('Digite o nome de sua cidade:')).capitalize().strip()
#cidade1 = cidade.split()
#print('A cidade {} começa com santo ?'.format(cidade))
#print('Santo' in cidade1[0])


#Segunda Opção

cidade = str(input('Digite o nome de sua cidade:')).strip()
print(cidade[:5].capitalize() == 'Santo')