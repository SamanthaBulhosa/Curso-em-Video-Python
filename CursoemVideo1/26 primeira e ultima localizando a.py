# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes apareceu a letra "A"
# - Em que posiçao ela apareceu a primeira vez
# - Em que posiçao ela apareceu a última vez

frase = str(input('Digite uma frase: ')).upper().strip()
n1 = frase.count('A')
print('A letra A aparece {} vezes na frase.'.format(n1))
n2 = frase.find('A')+1
print('A primeira letra A aparece na posicao {}'.format(n2))
n3 = frase.rfind('A')+1
print("A última letra A apareceu na posicao {}".format(n3))

# OBS: o +1 significa que vai conta os caracteres do 1 ate o fim e nao do 0, pq assim o resultado seria diferente
# O .upper() é se o usuario digitar em maiusculo ou menusculo vai identificar
# O .rfind('A') serviu para localizar do lado direito
