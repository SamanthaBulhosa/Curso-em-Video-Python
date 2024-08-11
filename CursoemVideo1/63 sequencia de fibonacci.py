# Escreva um programa que leia um número n inteiro qualquer e mostre na tela
# os n primeiros elementos de uma sequência de Fibonacci.
# Ex 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 o fibonacci sempre soma o numero anterior com o proximo
# e sempre vai comecar com 0 e 1

print('_' * 30)
print('Sequência de Fibonacci')
print('_' * 30)
num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')  # aqui está 0 e 1 ja que a sequencia começa assim
cont = 3  # esse conte vai do num 3 em diante
while cont <= num:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2  # t1 passa a ser t2 para poder somar com o proximo numero
    t2 = t3  # t2 passar a ser t3
    cont += 1
print('-> FIM')
print('~' * 30)
