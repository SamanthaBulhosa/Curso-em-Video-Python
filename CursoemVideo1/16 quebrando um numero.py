""" Crie um programa que leia um número Real qualquer pelo
teclado e mostre na tela a sua posição inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6."""

from math import trunc
num = float(input('Digite um número: '))
print("O número {} tem a parte inteira {}.".format(num, trunc(num)))

# Tem como fazer de 2 maneiras, uma usando a biblioteca e a outra somente com o "int" sem a biblioteca!

num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, int(num)))
