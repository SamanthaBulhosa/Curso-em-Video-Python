# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.

from random import randint


def sortear(lista):  # A minha função sorteia recebe a minha lista
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):  # for para contar 5 valores
        # lista.append(randint(1, 10))# adicione a lista 5 valores aleatórios que vai ser sorteado de 1 a 10,
        # nao vou usar dessa forma ja que preciso fazer um print com uma mensagem que irar exibir os números,
        # então irei criar uma variável num, para chamar na formatação da mensagem

        num = randint(1, 10)
        lista.append(num)
        print(f'{num}', end=' ')
    print('PRONTO')


def somarPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, a soma total dos pares são {soma}')


# Programa inicial

numero = list()
sortear(numero)  # Aqui eu conecto minha lista "numero" ao def através da função "sortear" / E EXIBO O COMANDO DO DEF. EXEMPLO: Sorteando 5 valores da lista: 1 10 4 4 3 PRONTO
# print(numero)  # nessa linha eu exibo os 5 valores sorteados a lista - exemplo: [8, 7, 1, 5, 9] / NAO PRECISO USAR ESSE JA QUE QUANDO EU CHAMO O DEF JA EXIBI O RESULTADO
somarPar(numero)  # Na def somarPar eu conector numero a lista. OBS SAMANTHA, lembra disso!