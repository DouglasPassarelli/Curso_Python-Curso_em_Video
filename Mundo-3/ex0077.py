palavras = ('aprender', 'progamar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'progamador', 'futuro')
for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra , end=' ')
    print()























'''''if 'a' in palavra:
        print(f'a ' * palavra.count('a'))
    if 'e' in palavra:
        print('e ' * palavra.count('e'))
    if 'i' in palavra:
        print('i ' * palavra.count('i'))
    if 'o' in palavra:
        print('o ' * palavra.count('o'))
    if 'u' in palavra:
        print('u ' * palavra.count('u'))'''







