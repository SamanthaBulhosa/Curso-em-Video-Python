# Desenvolva um programa que leia o primeiro termo e a razão de um PA.
# No final, mostre os 10 primeiros termos dessa progressão.

# Tentei entender que diabo é uma PA, tentei estudar para saber, so que piorou, odeio matematica
# Achei muito dificil mesmo depois que o professor fez!

termo = int(input('Primeiro termo: '))  # P.A é qualquer numero
razao = int(input('Digite a razao: '))  # A razao é o numero que vai ser pulado, ex: se for 5 vai pular 5 em 5
decimo = termo + (10 - 1) * razao  # Essa é a formula matematica para fazer o decimo e os demais...
for c in range(termo, decimo, razao):
    print('{}'.format(c), end='-> ')
print('Fim')


