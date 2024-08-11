# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

dados = dict()
gols = list()
some = 0
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(partidas):
    g = int(input(f'  Quantos gols na partida {c}? '))
    some += g
    gols.append(g)
    dados['gols'] = gols
    dados['total'] = some
print('=*=' * 30)
print(dados)
print('=*=' * 30)
for v, k in dados.items():
    print(f'O campo {v} tem o valor {k}.')
print('=*=' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas')
for conte, fez in enumerate(dados['gols']):  # Dificuldade para fazer isso, so entendi depois que o professor fez essa parte.
    print(f'  => Na partida {conte}, Fez {fez} gols')
print(f'Foi um total de {dados["total"]} gols.')

# CONSEGUIR FAZER SOZINHA! O problema é que nao consigo juntas as 2 linhas, mas a atividade fiz certo.
# Irei ver como o professor vai fazer, mas estou muito orgulhosa de ter conseguido fazer,
# já que estava sem programar a um tempo e não estava conseguindo resolver nenhum exercício...

# COMO O PROFESSOR FEZ!

jogador = dict()
partida = list()
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, total):
    partida.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partida[:]  # copiei o dado da partida[:] para dentro do dicionario [gols]
jogador['total'] = sum(partida)  # sum é para somar a partida sem precisar usar +=
print('-=-' * 30)
print(jogador)
print('-=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 30)
print(f'O jogador: {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  ==> Na partida {i}, fez {v} gols.')
print(f'Foi o total de {jogador["total"]} gols.')