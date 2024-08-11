# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de
# trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a = input('Primeiro nome: ')
b = input('Segundo nome: ')
c = input('Terceiro nome: ')
d = input('Quarto nome: ')
lista = [a, b, c, d]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)

# Duas formas de se fazer

import random
a = input('Primeiro nome: ')
b = input('Segundo nome: ')
c = input('Terceiro nome: ')
d = input('Quarto nome: ')
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))
