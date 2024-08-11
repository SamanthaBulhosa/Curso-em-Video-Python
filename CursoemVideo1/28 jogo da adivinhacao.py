# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para
# o usuario tentar descobrir qual foi o numero escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''from random import choice

num = [0, 1, 2, 3, 4, 5]
escolha = choice(num)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
eu = int(input('Digite qual numero voce acha que o computador escolheu: '))
print('O numero sorteado foi {}'.format(escolha))
if eu == escolha:
    print('Parabens vôce venceu!')
else:
    print('O computador venceu.')'''

# Eu conseguir sozinha!!! AAAAAAAAAAAAAA to feliz

# COMO O PROF FEZ ESTA ABAIXO

from random import randint
from time import sleep
computador = randint(0,5) # Faz com que o computador sortei um numero
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2) # esse comando faço com que espere 2 segundos para mostrar o resultado a seguir!
if jogador == computador:
    print('PARABÉNS, Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
