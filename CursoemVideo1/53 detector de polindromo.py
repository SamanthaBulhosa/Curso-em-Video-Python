# Crie um programa que leia uma frase qualquer e diga se ela é um palindrome,
# desconsiderando os espaços.
# Ex: apos a sopa se ler de tras para frente é palindrome

# Usando o fatiamento

frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.strip()
juntar = ''.join(separar)
inverter = juntar[::-1]
print('O inverso de {} é {}'.format(juntar, inverter))
if inverter == juntar:
    print('Temos um palíndrome!')
else:
    print('A frase digitada não é um palíndrome!')

# poderia usar logo abaixo de inverso o seguinte codigo, que também
# daria o mesmo resultado so que usando mais linha de codigo, usando o FOR
inverter = ''
for letra in range(len(juntar) - 1, - 1, - 1):
    inverter += juntar[letra]