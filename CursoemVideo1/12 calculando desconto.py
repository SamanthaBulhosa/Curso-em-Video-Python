# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual o preço do produto: R$'))
d = p - (p * 5 / 100)
print('O produto que custava R${} na promoção com o desconto de 5% vai custar {:.2f}'.format(p,d))

# Caso precise alterar o valor do desconto só mudar em (p * 15 / 100) assim estará com 15% de desconto!