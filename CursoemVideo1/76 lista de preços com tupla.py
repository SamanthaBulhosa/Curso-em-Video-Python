# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produto = ('Lápis', 1.75,
           'Borracha', 2.00,
           'Caderno', 15.90,
           'Estojo', 25.00,
           'Transferidor', 4.20,
           'Compasso', 9.99,
           'Mochila', 120.00,
           'Canetas', 22.30,
           'Livros', 34.90)
print('-' * 50)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)
for posiçao in range(0, len(produto)):  # vai começar 0 até o tamanho do produto com o len
    if posiçao % 2 == 0:
        # aqui eu verifico se a posicao do produto é par
        # e se for par eu posso manipular e colocar a direita.
        # OBS: os preços estao na posicao impar e o nome do produto é par
        print(f'{produto[posiçao]:.<30}', end='')
        # O .<30 eu coloco 30 pontinho dentro desse espaço
    else:
        print(f'R${produto[posiçao]:>7.2f}')
        # OBS: o >10 eu dou um espaço no valor do produto para a direita
        # O .2f eu coloco a casa decimal
print('-' * 50)

