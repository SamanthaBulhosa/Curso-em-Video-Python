# Um professor quer sortear um dos alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
a = input('Primeiro nome: ')
b = input('Segundo nome: ')
c = input('Terceiro nome: ')
d = input('Quarto nome: ')
lista = [a, b, c, d]
escolha = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolha))

# Abaixo eu importei somente da biblioteca random o choice, e acima eu importei toda a biblioteca

from random import choice
a = input('Primeiro nome: ')
b = input('Segundo nome: ')
c = input('Terceiro nome: ')
d = input('Quarto nome: ')
lista = [a, b, c, d]
escolha = choice(lista)
print('O aluno escolhido foi {}'.format(escolha))
