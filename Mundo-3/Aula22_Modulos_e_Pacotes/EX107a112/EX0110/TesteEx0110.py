'''
Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
'''

#Funções em moeda.py

from EX107a112 import moeda

p = float(input('Digite um valor: R$ '))
moeda.resumo(p, 50, 10)