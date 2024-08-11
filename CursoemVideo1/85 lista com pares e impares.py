# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e impares. No final mostre
# os valore pares e impares em ordem crescente.

'''temporario = list()
for num in range(0, 3):
    temporario.append(int(input(f'Digite o {num + 1}º valor: ')))
    if num % 2 == 0:
        temporario.append(temporario[:])
    elif num % 3 == 1:
        temporario.append(temporario[:])
    temporario.clear()
print(f'Os valores PARES foram {temporario}')
print(f'Os valore ÍMPARES foram {temporario}')
print(f'Ordem: {enumerate(temporario)}')'''

# Nao conseguir fazer, o resultado dá errado exemplo o 5 dar como par.
# E quando mostra o resultado vejo uma lista está dentro da outra por conta [[]]

# COMO O PROFESSOR FEZ.

num = [[], []]  # temos uma lista dentro outra lista, ''[[0], [1]] aqui tenho uma lista e 2 listas internas''
valor = 0
for c in range(1, 8):
    valor = (int(input(f'Digite um {c}° valor: ')))
    if valor % 2 == 0:
        num[0].append(valor)  # na lista num interno eu coloco na posição 0 os valores pares.
    else:
        num[1].append(valor)  # na lista num interno eu coloco na posição 1 os valores impares.
num[0].sort()  # coloca na ordem crescente os números pares
num[1].sort()
print(f'pares {num[0]}')
print(f'impares {num[1]}')

