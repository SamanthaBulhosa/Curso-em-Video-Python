# Faça um programa que jogue par ou impar com o computador.
# O jogo so será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    escolha = ' '
    while escolha not in 'PI':  # Aqui vou verificar se a escolha foi P ou I
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')  # aqui vai escolher a frase se deu par ou impar!
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if soma % 3 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
