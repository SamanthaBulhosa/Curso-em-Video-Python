# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é maior
# O segundo valor é maior
# Nao existe valor maior, os dois sao iguais

num0 = int(input('Primeiro valor: '))
num1 = int(input('Segundo valor: '))
if num0 > num1:
    print('O PRIMEIRO valor é maior')
elif num1 > num0:
    print('O SEGUNDO valor é maior')
elif num0 == num1:
    print('Nao existe valor maior, os dois sao IGUAIS')

# Conseguir resolver sozinhaaa :D

# Professor fez:
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')

