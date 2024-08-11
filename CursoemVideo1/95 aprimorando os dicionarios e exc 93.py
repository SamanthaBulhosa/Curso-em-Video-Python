# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
partida = list()
time = list()
while True:
    jogador.clear()  # limpo por que a cada laço eu vou ler um dado de um novo jogador
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partida.clear()  # preciso limpar a partida porque aqui ele esta acumulando os dado e vai ser exibido esse acumulo se nao limpar.
    # lista partida tem o valor que está conectada ao dicionário em jogador['gols'] onde fiz uma cópia,
    # e adicionei tudo a segunda lista que é time, por tanto "partida" e "gols" então copiada a lista time.
    for c in range(0, total):
        partida.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())  # nao posso fazer fatiamento dentro de dicionários
    while True:
        resp = str(input('Quer continuar? S/N]: ')).upper()[0]
        if resp in 'SN':  # Se resposta nao for S ou N mostre a msg de erro e repita a pergunta!
            break
        print('ERRO! responda apenas S ou N.')
    if resp == 'N':  # se resposta for N break e saia do loop.
        break
print('=-*-=' * 15)  # DIFÍCIL DE FAZER DAQUI PARA BAIXO.
print(' cod ', end='')
for i in jogador.keys():
    print(f'{i:<8}', end='')  # alinha para a direita as chaves {cod   nome      gols     total}
print()
print('_' * 30)
for k, v in enumerate(time):  # espaços entre um valor e outro
    print(f'{k:4} ', end='')
    for d in v.values():
        print(f'{str(d):<7}', end='')  # alinha para a direita os valores {0 Sam [3, 2] 5}
    print()
print('=-*-=' * 15)
while True:
    cod = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    if cod == 999:
        break
    if cod >= len(time):  # se o cod que o usuário inserir for maior ou igual ao tamanho do time, faça:
        print(f'ERRO! Não existe jogador com código {cod}!')
    else:
        print(f' --[ LEVANTAMENTO DO JOGADOR(A) {time[cod]["nome"].upper()} ]--')  # O jogador está dentro de time, e o índice numérico está no cod,
        # e dentro dele eu tenho o ["nome"] que está dentro do dicionário.
        for i, g in enumerate(time[cod]['gols']):
            print(f'     No jogo {i + 1} fez {g} gols.')
    print('---' * 25)
print('Fim do programa!')