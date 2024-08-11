# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
# dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = dict()
lista = list()
pessoas = some = maior = menor = c =0
while True:
    dados.clear()
    dados['nome'] = (str(input('Nome: ')))
    dados['sexo'] = (str(input('Sexo: [F/M] '))).upper().strip()
    while dados['sexo'] not in 'MF':
        print('ERRO! por favor, digite apenas M ou F.')
        dados['sexo'] = (str(input('Sexo: [F/M] '))).upper().strip()
    if dados['sexo'] == 'F':
        lista.append(dados['nome'])
    dados['idade'] = (int(input('Idade: ')))
    lista.append(dados.copy())
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    c += 1
    pessoas += dados['idade']
    some = pessoas / c
    while resp not in 'NS':
        print('ERRO! responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break  # a estrutura acima conseguir fazer sozinha :D
print(dados)
print('=-=' * 30)
print(f'A) O grupo tem {c} pessoas.')  # conseguir
print(f'B) A média de idade é de {some} anos.')  # conseguir
print(f'C) As mulheres cadastradas foram: {lista}')  # conseguir exibindo em forma de lista, e o prof fez diferente
print(f'Lista das pessoas que estão acima da média:')
for k, v in dados.items():  # nao conseguir! preciso colocar as pessoas com a maior idade aqui.
    print(f'  {k} = {v};', end='')
print()
print('<< FIM DO PROGRAMA >>')

# COMO O PROFESSOR FEZ:

dicionario = dict()
lista = list()
soma = media = 0
while True:
    dicionario.clear()  # por conta do loop faço a limpeza do dicíonario ja que abaixo insiro as informações na lista
    dicionario['nome'] = str(input('Nome: '))
    while True:
        dicionario['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]  # método upper deixa a letra maiúscula e [0] para pega a primeira letra
        if dicionario['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F.')
    dicionario['idade'] = (int(input('Idade: ')))
    soma += dicionario['idade']
    lista.append(dicionario.copy())  # na lista eu adiciono o dicionário e faço a copía dos dados para a lista
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if resp == 'N':
        break
print('=-=' * 30)  # DA LINHA 65 PARA CIMA É A LEITURA DOS DADOS, E JA A LINHA 66 PARA BAIXO ESTOU ANALISANDO OS DADOS.
print(f'A) Ao todo {len(lista)} pessoas cadastrada.')  # len(lista) é tamanho da lista, que serve como contado
media = soma / len(lista)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastrada foram ', end='')
for p in lista:  # SAMANTHA, PRESTA ATENÇÃO NESSA PARTE DO CÓDIGO!
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in lista:  # NÃO CONSEGUIR ENTENDER MUITO BEM O ESSE RESULTADO, COMO O "P" SE TRANSFORMOU EM DICIONARIO?
    if p['idade'] >= media:
        print('')
        for k, v in p.items():  # NUNCA PENSARIA NESSA SOLUÇÃO.
            print(f'{k} = {v};', end='')
        print()
print('>>>  Fim do programa! <<<')
# --- print(lista)  # na lista consigo visualizar todas as informações inseridas pelo usuário
# lista[{'nome': 'sAM', 'sexo': 'F', 'idade': 26}, {'nome': 'maria', 'sexo': 'F', 'idade': 9}]
# --- print(dicionario)  # ja no dicionário so consigo visualizar ultima informação inserida
# dicionario {'nome': 'maria', 'sexo': 'F', 'idade': 9}
# para ficar mais claro de entender: