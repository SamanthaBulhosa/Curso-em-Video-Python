# Faça um programa que leia um número inteiro e diga se ele é ou nao um número primo
# Numero primo ele so é divissivel por 1 e por ele mesmo. ex: 5 é divisivel por 1, sobra 1 ja o 6 nao

num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[1:m número {} foi divisível {} vezes'.format(num, total))
if total == 2:
    print('E por isso ele È PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
