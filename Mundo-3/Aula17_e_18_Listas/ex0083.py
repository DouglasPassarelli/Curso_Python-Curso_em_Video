'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada 
está com os parênteses abertos e fechados na ordem correta.
'''

expre = list()
expre.append(str(input('Digite um expressão: ')))
cont = 0
for c in expre:
    for l in c:
        if l == '(':
            cont += 1
        elif l == ')':
            cont -= 1
if cont == 0:
    print('A expreção esta valida!')
else:
    print('A expreção esta valida!')

