# Refaça o desafio 51, lendo o primeiro termo e a razao de uma PA,
# mostrando os 10 primeiros termos da progressao usando a estrutura while.

print('Gerador de PA')
print('¨¨' * 15)
termo = int(input('Primeiro termo: '))  # P.A é qualquer numero, que vai começar ex, 3 ate a razao onde vai ser pulada
razao = int(input('Digite a razao: '))  # A razao é o numero que vai ser pulado, ex: se for 5 vai pular 5 em 5
cont = 1
while cont <= 10:
    print('{}'.format(termo), end='-> ')
    cont += 1
    termo += razao
print('Fim')
