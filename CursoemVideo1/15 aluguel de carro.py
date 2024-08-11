# Escreva um programa que pergunte a quantidade de KM percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado calcule o preço a
# pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
soma = (dias * 60) + (km * 0.15)
print('O valor a pagar é de R${:.2f}'.format(soma))
