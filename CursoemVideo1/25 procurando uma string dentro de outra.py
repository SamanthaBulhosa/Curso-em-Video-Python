# Crie um programa que leia o nome de uma pessoa e diga se tem o "SILVA" no nome.

nome = str(input('Qual o seu nome completo: ')).strip()
tem = 'silva' in nome.lower()
print('Seu nome tem Silva? {}'.format(tem))

# Existe 2 formas de ter o mesmo resultado

nome = str(input('Qual o seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

# Usando o upper(maiuscula) ou lower(menuscula) o usuario pode digitar de qualquer jeito que o nome aparece
# ATENÇAO se eu colocar 'Silva' in nome.lower() eu vou precisar deixar o S do silva em menusculo
