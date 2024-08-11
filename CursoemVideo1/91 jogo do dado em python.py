# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
# em ordem, sabendo que o vencedor tirou o maior número no dado.

"""from random import randint
from time import sleep
dados = dict
print('---- Valores sorteados ---- ')
for dados['jogador'] in range(4):
    num = randint(1, 6)
    print(f'O Jogador({dados["jogador"] + 1}) tirou {num} no dado')
    sleep(1)
print('---- Ranking dos jogadores ---- ')  # NAO CONSIGO RESOLVER ESSA PARTE, PARA MOSTRAR A ORDEM DOS RANKING
for p, j in enumerate(dados):
    print(f'{p + 1}° lugar: {j} com {dados["jogador"]}')
"""
from random import randint
from time import sleep
from operator import itemgetter
dados = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
for k, v in dados.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('---- Ranking dos jogadores ---- ')
for p, j in enumerate(ranking):
    print(f'{p +1}° lugar: {j[0]} com {j[1]}')
    sleep(1)