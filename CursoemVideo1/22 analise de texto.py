# Crie um programa que leia o nome completo de uma pessoa e mostre:

# - Nome com todas as letras maiúscula
# - Nome com todas em menúscula
# - Quantas letras ao tod (sem considerar espaços)
# - Quntas letras tem o primeiro nome

nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em menúsculo é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
# Abaixo teremos o mesmo resultado do print a cima da ultima linha!!!
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0], len(nome.split()[0])))


# Com esse comando consigo tirar todos os espaços e tmb o do meio >>> .format(len(nome) - nome.count(' '))) <<<
