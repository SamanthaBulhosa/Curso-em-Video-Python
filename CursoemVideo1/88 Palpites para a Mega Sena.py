# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

""" from random import randint
jogo = [0, 0, 0, 0, 0, 0]
sortei = randint(0, 60)
jogo.append(sortei)
print('=-' * 20)
print('{:^40}'.format('JOGO DA MEGA SENA'))
print('=-' * 20)
pergunta = int(input('Quantos jogos você quer que eu sorteie? '))
print('{:^40}'.format(f'SORTEANDO {pergunta} JOGOS'))
for pergunta in range(pergunta):
    print(f'Jogo {pergunta +1}: {jogo}')"""

# NAO CONSEGUIR RESOLVER A PARTE DE MOSTRAR OS 6 NÚMEROS E QUE NAO SE REPITA

'''from random import randint
lista = list()
jogo = list()
cont = 0
while True:
    num = randint(1, 60)
    if num not in lista:  # se o número sorteado nao estiver em lista eu vou verificar nesse comando e add logo abaixo
        lista.append(num)  # adiciona o num a lista
        cont += 1
    if cont >= 6:  # aqui eu delimitei para ser até 6, então vai mostrar 6 num aleátorio se eu alterar para 10 vai mostrar 10 num aleatorio.
        break
lista.sort()  # para organizar em ordem crescente.
jogo.append(lista[:])  # na lista de jogo eu add a lista e faço a copía.
lista.clear()
print('=-' * 20)
print('{:^40}'.format('JOGO DA MEGA SENA'))
print('=-' * 20)
pergunta = int(input('Quantos jogos você quer que eu sorteie? '))
print('{:^40}'.format(f'SORTEANDO {pergunta} JOGOS'))
for pergunta in range(pergunta):
    print(f'Jogo {pergunta +1}:{jogo}')'''

from random import randint
from time import sleep

lista = list()
jogo = list()
print('=-' * 20)
print('{:^40}'.format('JOGO DA MEGA SENA'))
print('=-' * 20)
pergunta = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
print('=-=' * 5, f'SORTEADO {pergunta} JOGOS', '=-=' * 5)
while total <= pergunta:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:  # se o número sorteado nao estiver em lista eu vou verificar nesse comando e add logo abaixo
            lista.append(num)  # adiciona o num a lista
            cont += 1
        if cont >= 6:  # aqui eu delimitei para ser até 6, então vai mostrar 6 num aleátorio se eu alterar para 10 vai mostrar 10 num aleatorio.
            break
    lista.sort()  # para organizar em ordem crescente.
    jogo.append(lista[:])  # na lista de jogo eu add a lista e faço a copía.
    lista.clear()  # limpei a lista, e por conta do laço nao se repete o num
    total += 1
for i, l in enumerate(jogo):  # Enumerar a ordem colocando um em baixo do outro. O 'i' é um índice e 'l' sao as linhas de jogos.
    print(f"Jogo {i + 1}: {l}")
    sleep(1)  # para mostrar os números sorteados com um daley de 1 segundo
print('=-=' * 3, '< BOA SORTE! >', '=-=' * 3)
