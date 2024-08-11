# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da
# passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas.

# COMO EU FIZ
km = float(input('Qual a distancia da viagem em KM: '))
if km <= 200:
    km1 = 0.50 * km
    print('Ate 200KM o valor é R${:.2f}'.format(km1))
else:
    km2 = 0.45 * km
    print('Acima de 200KM o valor é R${:.2f}'.format(km2))

# COMO O PROFESSOR FEZ

distância = float(input('Qual a distancia da sua viagem? '))
print('Você está preste a começar um viagem de {}Km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preço))

# OBS: A variael preço pode ser usada 2x e com o if ele vai escolher (SAMANTHA ANALISA E LEMBRA DISSO)
