# Escreva um programa que leia um número inteiro qualquer e peça para o usúario
# escolher qual será a base de conversão:

# 1 para binario
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')

# Nao conseguir fazer, tive que ver o video para entender.
