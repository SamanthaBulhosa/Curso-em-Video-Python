# Faça um programa que leia 5 valores numéricos e guarde-os numa lista.
# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respetivas posições na lista.

valor = []
maior = menor = 0
for posicao in range(0, 5):
    valor.append(int(input(f'Digite um valor na posição {posicao}: ')))
print('=-=' * 15)
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {max(valor)} nas posições', end=' ')
print(valor.index(max(valor)))
print(f'O menor valor digitado foi {min(valor)} nas posições', end=' ')
print(valor.index(min(valor)))
print('=-=' * 15)
# conseguir sozinhaaa :D / se o usuario digitar 2 e depois 2
# nao conseguir mostrar a posição do segundo número

# COMO O PROFESSOR FEZ:
valor = []
maior = menor = 0
for posicao in range(0, 5):
    valor.append(int(input(f'Digite um valor na posição {posicao}: ')))
    if posicao == 0:
        maior = menor = valor[posicao]
    else:
        if valor[posicao] > maior:
            maior = valor[posicao]
        if valor[posicao] < menor:
            menor = valor[posicao]
print('=-=' * 15)
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}... ', end='')
print()
