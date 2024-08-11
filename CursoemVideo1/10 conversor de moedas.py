# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# Considere U$$ 1,00 = R$3,27

v = float(input('Quanto dinheiro você tem na carteira? R$'))
d = v / 5.03
e = v / 5.33
print('Com {} você pode comprar em Dólar US${:.2f}'.format(v, d))
print('Com {} você pode comprar em Euro €{:.2f}'.format(v, e))
print('Cotação feita 30/09/2023')
