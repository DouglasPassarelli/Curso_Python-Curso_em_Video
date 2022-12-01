# Faça um programa que calcule a soma entre todos os números impares
# que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500.

print('-=' * 10, 'Soma de Impares Multiplos de Tres', '-=' * 10)
print('Somando os numeros impares multiplos de tres em um intervalo de 1 a 500!')
soma = 0
c = 0
for cont in range(1, 501):
    if cont % 2 == 1 and cont % 3 == 0:
        c = c + 1
        soma = soma + cont
print('A soma de todos os {} numeros impares multiplos de tres e {}'.format(c, soma))
print('-=' * 10, 'FINALIZADO', '-=' * 10)
