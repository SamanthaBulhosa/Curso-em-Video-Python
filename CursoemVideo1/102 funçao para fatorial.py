# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# COMO EU FIZ:
def fatorial(num, show=False):
    # from math import factorial  (poderia usar a biblioteca math, mas quis fazer da forma tradicional)
    """
    -> Calcule o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1  # quando é um número limpo usamos 0, como o usuário já inseriu um número usar 1
    print('--' * 15)
    if show:
        while num > 0:
            print(f'{num}', end='')  # Vai do número que o usuário inseriu, exemplo: 5 ate 1
            print(' x ' if num > 1 else ' = ', end='')  # quando 'c' chegar no 1 vai colocar =
            f *= num
            num -= 1  # contou de 6 ate 1
        print(f'{f}')
    else:
        while num > 0:  # Se o num for maior que 0 faça:
            f *= num
            num -= 1
        print(f'{f}')


# Programa principal
fatorial(5, True)
help(fatorial)

# COMO O PROFESSOR FEZ:


def fatorial(n, show=False):
    """-> Calcule o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta.
    :return: O valor do Fatorial de um número n."""
    print('--' * 15)
    f = 1
    for c in range(n, 0, -1):  # inicie do 'n' e conte até 0 pulado de -1 em -1 de trás para frente
        if show:  # Se show for True, faça um print mostrando a formula 5 x 4 x 3 x 2 x 1 = 120
            print(c, end='')  # mostra os números contado de 'n' até 0
            if c > 1:  # Se 'c' que é meu contador for maior que 1 faça: mostre o x
                print(' x ', end='')
            else:  # Aqui é se 1 é menor que 0 faça: mostre =
                print(' = ', end='')
        f *= c  # Se (if show:) nao for False ele so mostra o resultado 120
    return f


print(fatorial(5, show=False))  # Se for False mostra o resultado: 120 / se for True mostra formula do fatorial: 5 x 4 x 3 x 2 x 1 = 120