# Aprimore o desafio anterior 86, mostrando no final:

# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = terceira_coluna = maior_valor = pares = 0
for linha in range(0, 3):  # esse for é para repetir 3x a pergunta dentro de cada sublist
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [L - {linha}][C - {coluna}]: '))
print('-*-' * 20)
for linha in range(0, 3):  # e esse for é para mostrar
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
        if matriz[linha][coluna] % 2 == 0:  # preciso colocar esse if dentro do for, estava fazendo abaixo,
            # e nao estava me gerando o resultado dos pares!
            soma_pares += matriz[linha][coluna]
    print()
print('-*-' * 20)
print(f'A soma de todos os valores pares digitados foi {soma_pares}')
for linha in range(0, 3):
    terceira_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna foi {terceira_coluna}.')
for coluna in range(0, 3):
    if coluna == 0:
        maior_valor = matriz[1][coluna]
    elif matriz[1][coluna] > maior_valor:
        maior_valor = matriz[1][coluna]
print(f'O maior valor da segunda linha foi {maior_valor}')


# muita dificuldade para fazer os exercícios, ficar sem praticar parece que nada mais faz sentido...
# vou refazer todos os exercício mbrar e compreender os demais que entao por vim.
#18/06/2024