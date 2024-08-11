# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

"""num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um número: ')))
    if num == 0:
        num.append(par)
    elif num == 1:
        num.append(impar)
        print(impar)
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if res == 'N':
        break
print('=-=' * 20)
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')"""

# NAO CONSEGUIR FAZER...

num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um número: ')))
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if res == 'N':
        break
for i, valor in enumerate(num):  # nao entendi o porque dessa linha (o i quer dizer indice)
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 2 == 1:
        impar.append(valor)
        print(impar)
print('=-=' * 20)
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
