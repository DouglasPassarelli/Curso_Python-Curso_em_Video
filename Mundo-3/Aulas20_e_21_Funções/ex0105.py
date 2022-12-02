''' 
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota      
– A menor nota
– A média da turma
– A situação (opcional)
'''

def notas(*num, sit=False):
    """
    -> Função para analisar varias notas e situação de varios alunos.
    :param num: uma ou maior notas de um aluno(aceita varias)
    :param sit: (opcional) sever para mostrar ou nao a situação do aluno
    :return: dicionario com varias informaçoes sobre a situação da turma
    """
    ava = {}
    ava['total'] = len(num)
    cont = maior = menor = media = 0
    for c in num:
        media += c
        if cont == 0:
            maior = c
            menor = c
        else:
            if c >= maior:
                maior = c
            elif c <= menor:
                menor = c
        cont += 1
    ava['maior'] = maior
    ava['menor'] = menor
    ava['media'] = media / ava['total']
    if sit:
        if ava['media'] >= 7:
            ava['Situação'] = 'BOA'
        elif ava['media'] >= 5:
            ava['Situação'] = 'RAZOAVEL'
        else:
            ava['Situação'] = 'RUIM'
    return ava


resp = notas(9, 2.5, 10, 6.5, sit=True)
print(resp)
help(notas)