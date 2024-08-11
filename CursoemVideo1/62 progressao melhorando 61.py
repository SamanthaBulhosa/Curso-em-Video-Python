# Melhore o desafio 61, perguntando para o usúario se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar O termos.

print('Gerador de PA')
print('¨¨' * 15)
termo = int(input('Primeiro termo: '))  # P.A é qualquer numero, que vai começar ex, 3 ate a razao onde vai ser pulada
razao = int(input('Digite a razao: '))  # A razao é o numero que vai ser pulado, ex: se for 5 vai pular 5 em 5
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end='-> ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
