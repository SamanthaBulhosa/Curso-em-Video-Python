# Crie uma tupla preenchida com os 20 primeiros colocandos da tabela
# do compeonato brasileiro de futebol, na ordem de colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

# OBS: pesquisar no Google a tabela do brasileirao.

print('{:-^80}'.format(''))
print('BRASILEIRÃO SÉRIE A')
times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense',
         'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro',
         'Vasco', 'Bahia', 'Santos', 'Goiás', 'Curitiba', 'América-MG')
print('{:-^80}'.format(''))
print(f'Lista de times do Brasileirão: {times}')
print('{:-^80}'.format(''))
print(f'Os 5 primeiros são: {times[:5]}')
print('{:-^80}'.format(''))
print(f'Os 4 ultimos são {times[-4:]}')
# print(f'Os 4 ultimos são {times[16:]}') eu fiz assim
print('{:-^80}'.format(''))
print(f'Times em order alfabética: {sorted(times)}')
print('{:-^80}'.format(''))
print(f'O {times[15]} esta na posição {times.index("Bahia")+1}°')
# OBS: o index eu localizo o time, a contagem começa 0 entao o bahia
# esta na posição 15, sendo na lista aparece na 16, por isso o +1
