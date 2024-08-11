# Faça um programa que calcule a soma entre todos os números impares que são multiplos de três
# e que se encontram no intervalo de 1 até 100.

soma = 0
cont = 0
for num_impar in range(1, 501, 2):
    if num_impar % 3 == 0:
        soma += 1
        cont += 1
        # cont = cont + 1  # aqui estou contando quandos
        # soma = soma + num_impar  # aqui estou acumulando a soma de todos os numeros
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))
