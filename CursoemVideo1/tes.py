produto = (('Lápis', 1.75), ('Borracha', 2.00,)
           #'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livros')
#preço = [1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.00, 22.30, 34.90]
print('-' * 50)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)
for lista in produto:
    print(f'', lista, '.' * 17, 'R$', preço[0], end=' ')
    print(f'', lista('Borracha'), '.' * 17, 'R$', preço[1], end=' ')
    # for tabela in preço:
    # print(lista, ('.' * 17), 'R$', tabela, end='\n')
print('Fim')
print('-' * 50)
