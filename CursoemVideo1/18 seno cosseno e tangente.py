""" Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo."""

# import math
from math import sin, cos, tan, radians
a = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, sen))
cos = cos(radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, cos))
tg = tan(radians(a))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(a, tg))

# OBS: utilizando o "import math" precisaria esta assim minha vareavel com os math em tods as linhas
# "sen = math.sin(math.radians(a))"
# ESTOU COM DIFICULDADE PARA SABER QUAL FUNÇAO USAR PARA FAZER O CALCULO!
