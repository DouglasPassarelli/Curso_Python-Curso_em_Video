''' Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar 999,
que é a condição de parada (flag).
No final, mostre quantos números foram digitados
e qual foi a acc entre eles (desconsiderando o flag)
'''

quant = soma = 0
while True:
    n = int(input('Digite um numero(999 para parar): '))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'Foram digitados um total de {quant} numeros, e a soma entre eles é {soma}')