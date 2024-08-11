# Faz 2 variáveis de inteiros e mostra
verdadeiro = int(10)
falso = int(9)
print(verdadeiro, falso)

# Compara essas 2 variáveis com 2 operadores de comparação diferentes e mostra
print(9 <= 10)
print(10 <= 9)

# Faz 2 operações aritméticas e mostra
print('-=' * 25)
print('''[ 1 ] Pagamento em númerario tem 10% de desconto!
[ 2 ] Pagamento no cartao de credito tem 20% de juros''')
print('-=' * 25)
preco = float(input('Digite o valor do produto: R$ '))
opcao = int(input('Qual a forma de pagamento? '))
desconto = preco - (preco * 10 / 100)
cartao = preco + (preco * 10 / 100)
if opcao == 1:
    print('Total a pagar R${:.2f}'.format(desconto))
    print('DESCONTO DE 10% APLICADO')
elif opcao == 2:
    print('Total a pagar R${:.2f}'.format(cartao))
    print('JUROS 10% NO CARTAO DE CREDITO')
elif opcao >= 3:
    print('Opção INVALIDA')
print('=-' * 25)
# Faz 2 operações de comparação e 1 operação lógica entre elas
n1 = 25
n2 = 20
print(25 != 20 or 25 > 20)

# Faz outras 2 operações de comparação e outra operação lógica entre elas
print(25 >= 20 and 25 == 20)

# Faz a potência de um número pelo outro
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# Faz a multiplicação de um número pelo outro
n = int(input('Digite um número para ver a tabuada: '))
print('-' * 14)
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('-' * 14)

# Faz a divisão de um número pelo outro
num1 = 10
num2 = 2
print('{} dividido por {} = {}'.format(num1, num2, (num1 / num2)))
