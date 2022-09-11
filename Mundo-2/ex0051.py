print('-=' * 10, 'Progressão artimetica', '-=' * 10)
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão de um PA: '))
for c in range(0, 10):
    print(termo, end=' --> ')
    termo = termo + razao
print('FINALIZADO')


#decimo termo de uma PA
#decimo = termo (10 - 1) * razao
#for c in range (termo, decimo + razao, razao):