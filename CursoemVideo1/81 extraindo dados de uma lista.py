# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print("-=-" * 20)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 FAZ parte da lista!')
else:
    print(f'O valor 5 NÃO foi encontrado na lista!')

# nao conseguir fazer
