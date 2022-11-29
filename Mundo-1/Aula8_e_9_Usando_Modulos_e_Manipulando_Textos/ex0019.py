# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
# programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido

import random
print('=' * 5, 'Sorteio', '='*5)
print('Aluno 01')
aluno01 = input('Nome do aluno:')
print('=' * 8)
print('Aluno02')
aluno02 = input('Nome do aluno:')
print('=' * 8)
print('Aluno03')
aluno03 = input('Nome do aluno:')
print('=' * 8)
print('Aluno04')
aluno04 = input('Nome do aluno:')
lista = [aluno01, aluno02, aluno03, aluno04]
print('=' * 15)
print('O aluno sorteado para apagar o quadro foi {}'.format(random.choice(lista)))
