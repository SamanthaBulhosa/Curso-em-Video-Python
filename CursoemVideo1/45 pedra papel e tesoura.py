# Crie um programa que faça o computador jogar Jokenpô com você. (pedra, papel e tesoura)

from random import randint  # escolha de numero aleatorio
from time import sleep  # faz com que o resultado demore para aparecer de acordo com o tempo colocado
item = ('Pedra', 'Papel', 'Tesoura')  # Se o computador escolher 2 vai trocar a palavra por tesoura
camputador = randint(0, 2)
print('''Suas Opção:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador > 2:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('POOO')
    print('=-' * 15)
    print('O computador jogou {}'.format(item[camputador]))  # Fazendo (inten[computador]) troco o numero pela palavra
    print('Jogador jogou {}'.format(item[jogador]))
    print('=-' * 15)
    if camputador == 0:  # computador jogou PEDRA
        if jogador == 0:
            print('IMPATOU')
        elif jogador == 1:
            print('JOGADOR GANHOU')
        elif jogador == 2:
            print('COMPUTADOR VENCEU')
    elif camputador == 1:  # computador jogou PAPEL
        if jogador == 0:
            print('COMPUTADOR GANHOU')
        elif jogador == 1:
            print('IMPATOU')
        elif jogador == 2:
            print('JOGADOR GANHOU')
    elif camputador == 2:  # computador jogou TESOURA
        if jogador == 0:
            print('JOGADOR GANHOU')
        elif jogador == 1:
            print('COMPUTADOR GANHOU')
        elif jogador == 2:
            print('IMPATOU')
