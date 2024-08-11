teste = list()
teste.append('Samantha')
teste.append(26)
pessoas = list()
pessoas.append(teste[:])  # utilizado o [:] eu faço uma copía, fazendo assim nao se repete a lista
teste[0] = 'Raiana'
teste[1] = 24
pessoas.append(teste[:])
print(pessoas)

galera = [['Yasmim', 25], ['Paloma', 28], ['Samantha', 26], ['Josenilda', 61]]
#             0       1        0      1       0         1         0        1
#                0              1                2                   3
print(galera[0])  # so vai mostrar o nome e a idade
print(galera[2][0])  # so vai mostrar o nome

for p in galera:
    # print(p) # vai criar uma lista com os nome e idades
    # print(p[0]) # se eu quiser somente os nomes das pessoas sem a idade so colocar [0]
    print(f'{p[0]} tem {p[1]} anos.')

print('=' * 20)

grupo = list()
dados = list()
maior = menor = 0
for cont in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    grupo.append(dados[:])
    # eu preciso usar [:] para fazer a copía dos dados, senão sera apagado ja que o comando
    # abaixo é de limpar.
    dados.clear()  # apaga os dados cada vez que faz o laço
print(grupo)

for p in grupo:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores.')
