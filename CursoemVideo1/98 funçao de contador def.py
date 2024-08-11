# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

# COMO EU FIZ
from time import sleep


def conte():
    print("---" * 15)


conte()
print('Contagem de 1 até 10 de 1 em 1')
for crescente in range(1, 11):
    print(crescente, end=' ')
    sleep(0.5)
print('FIM!')
conte()
print('Contagem de 1 até 0 de 2 em 2')
for crescente in reversed(range(0, 11, 2)):
    print(crescente, end=' ')
    sleep(0.5)
print('FIM!')
conte()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
conte()
print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
for c in range(inicio, fim, passo):
    if passo >= -0:
        for d in reversed(range(inicio, fim, passo)):
            print(d, end=' ')
    else:
        print(c, end=' ')
        sleep(0.5)
print('FIM')


# SEI QUE DAR PARA FAZER ESSA REPETIÇÃO DENTRO DO DEF JA QUE TENHO VÁRIAS LINHAS REPETIDAS,
# MAS NAO ESTOU CONSEGUINDO ACHAR UMA SOLUÇÃO PARA FAZER ISSO, IREI VER COMO O PROFESSOR FEZ
# PARA TER UMA NOÇÃO MELHOR DE COMO USAR O DEF.

from time import sleep


def contador(inicio, fim, passo):
    # preciso colocar esse teste logico antes, para validar o passo, porque tenho o passo positivo e negativo.
    if passo < 0:  # C) se o número de passo for menor que 0, exemplo -1 ou -3 em diante ele vai fazer:
        passo *= -1  # passo multiplicado por -1
    if passo == 0:  # Se o passo for igual a 0 faça
        passo = 1  # Passo recebe 1
    print('-=-' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')  # Contagem de 1 até 10 de 1 em 1 / Contagem de 10 até 0 de 2 em 2
    if inicio < fim:  # A) Se meu ínicio for menor que meu fim, faça:
        cont = inicio  # Crio uma variável cont que recebe = inicio (cont vai contar do ínicio)
        while cont <= fim:  # Enquanto cont for menor ou igual ao fim, faça:
            # print(f'{cont}', end=' ', flush=True) O professor fez assim no código dele ja que estava dando um delay ao contar, ja no meu nao foi preciso, devido atualização do pycharm!
            print(f'{cont}', end=' ')  # Aqui eu tenho o cont que está contando do inicio ate chegar no fim.
            sleep(0.5)  # conta lentamente os valores
            cont += passo  # cont mais passo, (se o passo for 3 meu cont recebe + 3 e vai ser contado em 3 em 3)
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM')


# PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('-=-' * 20)
print('Agora é sua vez de personalizar a contagem!')
inic = int(input('ìnicio: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
contador(inic, fi, pas)  # meu contador recebe o input da pergunta feita para o usuário, e preenche os campos acima no def.

# Achei um pouco difícil de fazer.