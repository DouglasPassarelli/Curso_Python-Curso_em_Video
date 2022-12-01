''' Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.'''

print('-=' * 10, 'Progressão artimetica', '-=' * 10)
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão de um PA: '))
for c in range(0, 10):
    print(termo, end=' --> ')
    termo = termo + razao
print('FINALIZADO')


