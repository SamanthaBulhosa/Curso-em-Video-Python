# Escreve um programa que converta uma temperatura digitada em °C e converta para °F.

c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 35
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F'.format(c, f))
