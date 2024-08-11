# Crie um programa que leia dois valores e mostre um menu na tela:

# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
opcao = 0
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
while opcao != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
''')
    print('==-==' * 10)
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} + {} = {}'.format(num1, num2, soma))
    elif opcao == 2:
        mult = num1 * num2
        print('A multiplicação {} x {} = {}'.format(num1, num2, mult))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior valor é {}'.format(num1, num2, maior))
    elif opcao == 4:
        print('Quais são os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizado...')
    else:
        print('Opção inválida. Tente novamente.')
    print('==-==' * 10)
    sleep(2)
print('Fim do programa, volte sempre!')
