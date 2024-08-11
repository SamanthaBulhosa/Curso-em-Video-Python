# Melhore o jogo do desafio 28 onde o computador "pensar" em um número entre 0 e 10. Só
# que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
palpite = 0
acertou = False
print('Sou seu computador... \n'
      'Acabei de pensar em um número entre 0 a 10. \n'
      'Será que você consegue adivinhar qual número pensei?')
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('Mais... Tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpite))

# Como o PROFESSOR fez:

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 a 10.')
print('Será que você consegue adivinhar qual número pensei?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpite))
