alunos = {}
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Media de {alunos["nome"]}: '))
print('-=' * 20)
if alunos['media'] > 7:
    alunos['situação'] = 'Aprovado'
elif 5 <= alunos['situação'] < 7:
    alunos['situação'] = 'Recuperção'
else:
    alunos['situação'] = 'Reprovado'
print(f'      -- Nome e igual a {alunos["nome"]}')
print(f'      -- Media e igual a {alunos["media"]}')
print(f'      -- Situação e igual a {alunos["situação"]}')