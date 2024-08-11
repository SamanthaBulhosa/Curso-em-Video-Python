# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print('Os números pares são:')
for num_par in range(1, 51):
    num = num_par % 2
    if num == 0:
        print(num_par, end=' ')
# Conseguir sozinha <3 (O MEU CÓDIGO ESTA OCUPANDO ESPAÇO, O DO PROF FICOU MELHOR E SIMPLES)
print('\n')

# Como o PROFESSOR FEZ:
for num in range(2, 51, 2):  # vai do 2 até 51 so que pulando em 2 em 2 e sem ocupar espaço
    print(num, end=' ')
print('\n')

# NAO FAZER ASSIM (OCUPA MUITO ESPAÇO)
for n in range(1, 51):  # Fazendo dessa forma ocupa tempo e espaço na memória, pq vai ter que pular 2 em 2
    print('.', end='')  # Samantha executa esse código para lembrar, vai mostrar:  ..2..4.. a onde tem o . ocupa espaço
    if n % 2 == 0:      # eu consigo nao ocupar esse espaço fazendo da forma que estar abaixo no próximo código.
        print(n, end='')
print(' Acabou')
