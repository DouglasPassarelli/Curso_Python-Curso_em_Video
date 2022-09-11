#cidade = str(input('Digite o nome de sua cidade:')).capitalize().strip()
#cidade1 = cidade.split()
#print('A cidade {} começa com santo ?'.format(cidade))
#print('Santo' in cidade1[0])


#Segunda Opção

cidade = str(input('Digite o nome de sua cidade:')).strip()
print(cidade[:5].capitalize() == 'Santo')