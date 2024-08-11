# ---------------------------- ( O QUE É INTERACTIVE HELP - (Ajuda interativa) )---------------------------------------
# Interactive Help (Ajuda interativa)

# A ajuda interativa é o manual do python.

help()  # utilizando essa função abre o console, help> onde eu posso perguntar para que serve exemplo:
# len e ele me retorna todas as funcionalidades do len, me dizendo o que dar para fazer.

# para sair é só digitar: quit
# que volta para o console

# --------------------------------------- ( O QUE É HELP(PRINT) )---------------------------------------------------
# Outra maneira de fazer se eu nao souber para que serve.

help(print)  # é a mesma coisa do exemplo acima, so que a diferença é que nesse coloquei dentro do help
# a duvída da funcionalidade e ele me retorna o resultado direto no console sem eu precisar digitar no console
# e termina o programa sem eu precisar digitar quit para sair.

# ----------------------------------------- ( O QUE É .__DOC__ )-----------------------------------------------------
# Outra maneira de saber a funcionalidade é utilizando .__doc__

print(input.__doc__)  # a diferença está na formatação do texto, resumindo a explicação de como funciona.
# Explicação do .__doc__

"""Leia uma string da entrada padrão. A nova linha final é removida.

A string de prompt, se fornecida, é impressa na saída padrão sem uma nova linha final antes de ler a entrada.

Se o usuário pressionar EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), gere EOFError.
Em sistemas *nix, readline é usado se disponível."""

help(input)  # diferença na formatação do texto.
# Explicação do help(input)

"""Ajuda sobre entrada de função interna em builtins de módulo:

input(prompt='', /)
Lê uma string da entrada padrão. A nova linha final é removida.

A string de prompt, se fornecida, é impressa na saída padrão sem uma
nova linha final antes de ler a entrada.

Se o usuário pressionar EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), gera EOFError.
Em sistemas *nix, readline é usado se disponível."""


# --------------------------------------- ( O QUE É DOCSTRINGS )---------------------------------------------------

# É uma string de documentação, e vimos acima o manual e documento sobre as das funcionalidades
# docstrings é a minha documentação, onde eu explico o que cada coisa é, para melhor entendimento do código.
# Abaixo vou explicar como esse trecho de código funciona, em outros projetos eu estava (# comentando) ao lado
# porque nao sabia dessa função.

def contador(i, f, p):  # para eu fazer o docstring eu preciso abrir três aspas duplas abaixo do meu def

    """
    — > Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: fim da contagem
    :param p: passo da contagem (pulado em x valor)
    :return: sem retorno
    """

    c = i
    while c <= f:
        print(f'{c} ', end=' ')
        c += p
    print('FIM! ')


contador(2, 10, 2)
# E quando eu executar o help(contador) ele vai me mostrar e explicação do que é cada coisa.
help(contador)

""" contador(i, f, p)
    — > Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: fim da contagem
    :param p: passo da contagem (pulado em x valor)
    :return: sem retorno"""


# --------------------------------------- ( O QUE É PARÂMETROS OPCIONAIS )---------------------------------------------------

def somar(a=0, b=0, c=0):
    # Se caso o usuário nao informa o valor de 'c'
    # nao vai gerar um erro ja que considerei o 'c' e os demais com 0, se o usuário digitar valor nenhum o resultado vai ser 0
    """
    — > Faz a soma de três valores e mostrar o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    Função criada por Samantha Bulhosa
    """

    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)  # A = 3, B= 2, C = 5 cada um recebe um valor e posso alterar a ordem também
somar(a=8, c=4)  # posso nomear os meus parâmetros, e b como nao esta ele recebe o valor 0 que esta no def


# --------------------------------------- ( O QUE É ESCOPO DE VARIÁVEIS )---------------------------------------------------

def teste(b):
    global a  # Se eu usar esse comando 'global' o meu 'a' global passa a ser o 8 que esta dentro de def e serve para fora do def também.

    a = 8  # Dentro de def defino o meu 'a' para recebe o valor 8, e meu 'a' fora do def é global permanece com o valor 5,
    # porem esse 'a' é escopo local que armazena o valor 8, resumindo eu tenho 2 variáveis so que uma local e a outra global

    b += 4  # O 'b' e o 'c' é um escopo local, porque so consigo usar ou somar eles dentro do def
    c = 2
    print(
        f'Letra "A" dentro vale {a}')  # Observe que o 'a' que esta fora do def ele preenche dentro do def com o valor 5, global
    print(f'Letra "B" dentro vale {b}')  # Já a o 'b' ele soma 5 + 4 que dar o resultado 9 que é local
    print(f'Letra "C" dentro vale {c}')  # Logo o 'c' dentro do def recebe o valor 2 e só mostra o valor 2


# OBS: o 'b' e 'c' so funciona dentro dessa aréa (def), se eu colocar fora do def dá erro por falta de escopo!


a = 5  # Esse 'a' está em um escopo global ja que consigo usar ele dentro do def e fora do def também.
teste(a)
print(f'Letra "A" fora vale {a}')  # escopo global


# --------------------------------------- ( O QUE É RETORNANDO VALORES )---------------------------------------------------

# O return é a personalização dos resultados

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s  # função com retorno


resp1 = soma(2, 3, 5)
resp2 = soma(2, 2, )
resp3 = soma(6)
print(f'Os resultados foram {resp1}, {resp2} e {resp3}')

