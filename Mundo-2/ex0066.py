quant = soma = 0
while True:
    n = int(input('Digite um numero(999 para parar): '))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'Foram digitados um total de {quant} numeros, e a soma entre eles é {soma}')