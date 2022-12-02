'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
'''

from EX111.UtilidadeCeV import moeda

p = float(input('Digite um valor: R$ '))
moeda.resumo(p, 50, 10)