# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:

# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves.


""" cadastrado = pesados = leves = 0
pessoas = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
    pessoas.append(dados[:])
    dados.clear()
    cadastrado += 1
    for p in pessoas:
        if p[1] > pesados:
            pesados = p[1]
        if p[1] < leves:
            leves = p[1]
    if continuar == 'N':
        break
print('=' * 25)
print(f'Ao todo, você cadastrou {cadastrado} pessoas')
print(f"As pessoas mais pesadas foram {max(pessoas[1])}Kg. peso de {pessoas[0][0]}")
print(f"As pessoas mais leves foram {min(pessoas[1])}Kg. peso de {pessoas[0][0]}")"""

# NAO CONSEGUIR FAZER, a parte do peso leve estou tendo dificuldade para mostrar

# COMO O PROFESSOR FEZ!

temp = []  # lista temporária
princ = []  # lista principal para armazenar os dados
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))  # adicionei o nome na lista de temp
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])  # copiei os dados que estavam em temp para a lista princ
    temp.clear()  # limpei todos os dados que estava no temp
    resp = str(input('Quer continuar?[S/N]:  ')).upper().strip()
    if resp in 'Nn':
        break
print('=' * 25)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')  # usei o len para contar quantas pessoas tem na lista.
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for pessoa in princ:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}')
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for pessoa in princ:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}')

