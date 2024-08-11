# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programadora', 'futuro')
for vogal in palavras:
    print(f'\nNa palavra {vogal.upper()} temos', end=' ')
    for letras in vogal:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')
