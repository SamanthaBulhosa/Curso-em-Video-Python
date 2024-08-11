# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date # importa a biblioteca de data
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0: # Se o usurio colocar 0 vai puxar a data atual do computador
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

# Achei dificil e nao entendi muito bem