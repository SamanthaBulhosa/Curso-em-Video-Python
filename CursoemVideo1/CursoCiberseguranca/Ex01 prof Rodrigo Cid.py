# Deverão criar uma variável string
nome = 'Samantha'

# Deverão mostrar o tamanho dessa string
tamanho = len(nome)
print(tamanho)

# Deverão mostrar a segunda letra da string
print(nome[1])

# Deverão mostrar entre a terceira letra e a quinta letra da string
print(nome[3:6])

# Deverão mostrar todas as letras até à quinta letra
print(nome[:6])

# Deverão mostrar todas as letras a partir das terceira letra
print(nome[3:])

# Deverão mostrar a string toda em letras grandes
print(nome.upper())

# Deverão mostrar a string toda em letras pequenas
print(nome.lower())

# Deverão fazer alteração da segunda letra por um "t"
print(nome.replace('S', 'T'))

# Deverão separar a string dentro de uma lista, onde o meio de separação são espaços brancos
print(nome.split(' '))

# Deverão concatenar duas strings diferentes e torná-la numa só, numa nova variável
nome = 'Samantha'
sobrenome = 'Bulhosa'
print(nome, ' ' + sobrenome)

# Mostrar as funcionalidades das funções de strings: capitalize(), isalpha() e find()
print(nome.istitle())
print(nome.isalpha())
print(nome.find('mantha'))
