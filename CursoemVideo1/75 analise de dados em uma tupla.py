# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final mostre

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares

num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
# OBS: acima eu coloquei tudo dentro de () isso torna uma tupla, e nela armazena os 4 valores.
print(f'Você digitou os valores {num}')
print(f'O valor 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 aparece na {num.index(3)+1}° posição')
else:
    print('O valor 3 NÃO foi digitado em nenhuma posição')
print(f'O valores pares digitados foram ', end='')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')

# Nao conseguir fazer, nao consigo fazer a tupla, nao mostra os numeros armazenados