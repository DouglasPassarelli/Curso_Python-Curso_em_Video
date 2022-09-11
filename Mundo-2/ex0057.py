resp = str(input('Informe seu Sexo: [M/F] ')).upper().strip()[0]
while resp != 'M' and resp != 'F':
    resp = str(input('Dados Invalidos! Por favor, Informe seu Sexo novamente: ')).upper().strip()[0]
if resp == 'M':
    print('Sexo M cadastrado com sucesso!')
else:
    print('Sexo F cadastrado com sucesso!')


#codigo do guanabara

'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MnFf':
    sexo = str(input('Dados Invalidos! Por Favor, Informe novamente seu sexo: ')).strip().upper()[0]
print('sexo {} cadastrado com sucesso!'.format(sexo))'''

