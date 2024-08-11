# Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:

# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartao: 5% de desconto
# - em ate 2x no cartao: preço normal
# - 3x ou mais no cartao: 20% de juros

print(('{:=^40}'.format(' LOJA BULHOSA '))) # = aparece ^ centraliza em 40 espaços, o numero determina a quantidade de espaço
produto = float(input('Qual o valor do produto: R$'))
dinheiro = produto - (produto * 10 / 100)
cartao = produto - (produto * 5 / 100)
cartao2x = produto
cartao3x = produto + (produto * 20 / 100)
print('=-=' * 20)
print('[ 1 ] À vista dinheiro/cheque: 10% de desconto {:.2f}'.format(dinheiro))
print('[ 2 ] À vista no cartao: 5% de desconto {:.2f}'.format(cartao))
print('[ 3 ] Em ate 2x no cartao: preço normal {:.2f}'.format(cartao2x))
print('[ 4 ] 3x ou mais no cartao: 20% de juros {:.2f}'.format(cartao3x))
print('=-=' * 20)
pagamento = int(input('Como desejá pagar? '))
if pagamento == 1:
    print('A vista o valor tem 10% DESCONTO R${:.2f}'.format(dinheiro))
    print('Valor da compra SEM DESCONTO {:.2f}'.format(produto))
elif pagamento == 2:
    print('A vista no cartao valor tem 5% DESCONTO R${:.2f}'.format(cartao))
    print('Valor da compra SEM DESCONTO {:.2f}'.format(produto))
elif pagamento == 3:
    parcela = cartao2x / 2
    print('Será parcelado em 2x no cartão SEM DESCONTO R${:.2f}'.format(parcela))
    print('Valor total R${:.2f}'.format(cartao2x))
elif pagamento == 4:
    parcela = int(input('Quantas parcelas vai ser? '))
    quanto = cartao3x / parcela
    print('A compra será parcelada em {}x de {:.2f} com juros'.format(parcela, quanto))
    print('Valor total da compra {:.2f}'.format(cartao3x))
    print('Valor da compra SEM DESCONTO {:.2f}'.format(produto))
else:
    print('OPÇAO INVALIDA de pagamento!')

# Conseguir sozinha

# Como o PROFESSOR FEZ:

print('{:=^40}'.format(' LOJA GUANABARA '))
preco = float(input('Preço das compras: R$'))
print('''FORMA DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('DESCONTO 10% aplicado')
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('DESCONTO 5% aplicado')
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de {:.2f} de COM JUROS'.format(totalparc, parcela))
else:
    print('OPÇÃO INVALIDA de pagamento!')
    total = preco
print('Sua compra de R${:.2f} vai custar R$${:.2f} no final.'.format(preco, total))