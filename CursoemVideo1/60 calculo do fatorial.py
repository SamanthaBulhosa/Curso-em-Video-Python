# Faça um programa que leia um número qualquer e mostre
# o seu fatorial usando o while e depois faça com o if.
# Ex: 5! = 5 x 4x3 x 2x1 = 120 (obs: vai do 5 até o 1, se fosse 10 iria até 1 multiplicando)


# Fazendo usando a biblioteca math
from math import factorial
num = int(input('Digite um número para\ncalcular seu Fatorial: '))
fatorial = factorial(num)
print('O fatorial de {} é {}'.format(num, fatorial))

# modo tradicional

n = int(input('Digite um número para\ncalcular seu Fatorial: '))
c = n
f = 1  # quando é um número limpo usamos 0, como o usuário já inseriu um número usar 1
print('Calculando {}! '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')  # Vai do número que o usuário inseriu ate 1
    print(' x ' if c > 1 else ' = ', end='')  # quando 'c' chegar no 1 vai colocar =
    f *= c
    c -= 1  # contou de 6 ate 1
print('{}'.format(f))

# Criando usando o for e while.
