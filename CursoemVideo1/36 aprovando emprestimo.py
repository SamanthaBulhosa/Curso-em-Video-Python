# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar

# Calcule o valor da prestaçao mensal, sanbendo que ela nao pode excerder 30% do salário ou entao o emprestimo será negado

casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)  # mutiplico o valor dos anos por 12 ex: 7 anos * 12
exceder = salario * 30 / 100  # aqui multiplico o salario e divido para tirar 30%
meses = anos * 12  # mostra os meses
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} '.format(casa, anos, prestacao))
print('Total de meses {}'.format(meses))
if prestacao >= exceder:
    print('Emprestimo NEGADO! lamentamos')
else:
    print('Empréstimo pode ser CONCEDIDO! {:.2f}'.format(prestacao))

# Tive um pouco de dificuldade em fazer a prestaçao, mas de resto eu conseguir! 11/11/2023