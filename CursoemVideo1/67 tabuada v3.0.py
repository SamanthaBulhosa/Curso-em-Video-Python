# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuario.
# O programa será interrompido quando o número solicitado for negativo.


while True:
    tabuada = int(input('Quer ver a tabuada de qual valor: '))
    if tabuada < 0:
        break
    for num in range(1, 11):
        print(f'{tabuada} x {num} = {tabuada * num}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')



