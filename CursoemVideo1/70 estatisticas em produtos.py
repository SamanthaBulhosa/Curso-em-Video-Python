# Crie um programa que leia o nome e o preço de varios produtos.
# O programa deverá perguntar se o usuario vai continuar. No final, mostre:

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

total_preço = soma_produto = maior_preco = menor_preco = quant = 0
produto_barato = ' '
print('BAZAR DO SAPO')
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    quant += 1
    total_preço += preco
    if preco > 1000:
        soma_produto += 1
    if quant == 1 or preco < menor_preco:  # Aqui eu simplifico o bloco abaixo do else
        menor_preco = preco
        produto_barato = produto
    # else:
        # if preco < menor_preco:
            # menor_preco = preco
            # produto_barato = produto
    contin = ' '
    while contin not in 'SN':
        contin = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if contin == 'N':
        break
print('{:-^40}' .format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {total_preço:.2f} \n'
      f'Temos {soma_produto} produtos custando mais de R$1000.00 \n'
      f'O produto mais barato foi {produto_barato} que custou {menor_preco:.2f}')

# Dificuldade para saber o menor preço, nao sei como achar dentro da lista de produto
