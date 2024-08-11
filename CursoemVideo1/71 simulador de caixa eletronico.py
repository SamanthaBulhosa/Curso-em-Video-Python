# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.

# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('BANCO SB')
sacar = int(input('Qual valor você quer sacar? R$'))
total_caixa = sacar
cédula = 50
total_cédula = 0
while True:
    if total_caixa >= cédula:
        total_caixa -= cédula
        total_cédula += 1
    else:
        if total_cédula > 0:
            print(f'Total de {total_cédula} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_cédula = 0
        if total_caixa == 0:
            break
print('Volte sempre!')

# Achei muito difícil para entender a lógica! depois preciso refazer.