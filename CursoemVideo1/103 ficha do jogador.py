# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá mostrar a ficha
# do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez  {gols} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Números de Gols: '))
if g.isnumeric():  # usando o isnumeric eu consigo verificar se foi digitando o número ou não.
    g = int(g)  # 'g' recebe tipo 'int', ja que acima coloquei como str caso o usuário escreva o valor
else:
    g = 0  # se 'g' nao for um número 'int' ele recebe 0
if n.strip() == '':  # o strip remover espaços em branco no início e no final de uma string, se 'n' for igual 'nada digitado'.
    ficha(gols=g)  # exiba somente o número de gols
else:
    ficha(n, g)
