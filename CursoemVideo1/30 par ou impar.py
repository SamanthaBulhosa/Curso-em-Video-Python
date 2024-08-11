# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = int(input('Me diga um número qualquer: '))
resp = num % 2  # Dividir o número por 2 mostrando se restava 0 ou 1 e usando no if
if resp == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))

