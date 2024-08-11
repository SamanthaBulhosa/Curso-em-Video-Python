# ----------------- FUNÇÃO (PARTE 1) ------------------

# Função é uma funcionalidade, que usamos diariamente, por exemplo print(),input(),int(),float() e etc...
# como eu posso criar uma função, exemplo: mostrarlinha(), todas as funções em python é identificada por (parênteses) no fim do nome
# o que é def: definição de função, que é personalizado fazendo uma rotina no código.
# E para otimizar isso, eu escrevo apenas uma vez a minha função e da seguinte forma.

"""def mostrarlinha():  # sem parametro
    print('----' * 10)  # o print precisa está deslocado para dentro do def (tem que ser feito uma indentação)


mostrarlinha()
print('SISTEMA DE ALUNOS')
mostrarlinha()
mostrarlinha()
print('CADASTRO DE FUNCIONÁRIOS')
mostrarlinha()
mostrarlinha()
print('ERRO DO SISTEMA')
mostrarlinha()"""

"""def titulo(txt):  # com paramêtro
    print(txt)


titulo('SISTEMA DE ALUNOS')
titulo('Samantha')"""

"""a = 4
b = 5
s = a + b
print(s)  # resultado: 9
print('--' * 10)"""

# PASSANDO PARAMETROS

"""soma(5, 3)

# posso fazer explicito
soma(a=4, b=5)  # e também posso alterar a ordem ex: soma(b=4, a=5)"""

"""def soma(a, b):
    print(f'A = {a} e B = {b}')  # da para fazer formatado
    s = a + b
    print(f'A soma vale A + B = {s}')

soma(4, 3)"""

# EMPACOTADOR PARAMETROS *

"""def contador(* num): # O empacotamento é feito pelo "*"
   print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6)

vai ser exibido assim:
(2, 1, 7)
(8, 0)
(4, 4, 7, 6)

# Acima, cria uma tupla com todos os valores, e eu consigo fazer tudo que dar como tupla, lembrando que tupla nao é multavel."""

"""def contador(* num): 
    for valor in num:
        print(f'{valor}', end=' ')
    print('Fim')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6)

vai ser exibido assim:
2 1 7 Fim
8 0 Fim
4 4 7 6 Fim"""

"""def contador(*num): 
    tamanho = len(num)
    print(f'Recebir os valores {num} e são ao todo {tamanho} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6)

# vai ser exibido assim:
Recebir os valores (2, 1, 7) e são ao todo 3 números
Recebir os valores (8, 0) e são ao todo 2 números
Recebir os valores (4, 4, 7, 6) e são ao todo 4 números"""

# ISSO NÃO É UM DESEMPACOTAMENTO
def duplique(lista):  # fiz uma função "duplique" e coloquei o parametro "lista"
    pos = 0
    while pos < len(lista):  # enquanto o tamanho da minha lista for menor, faça
        lista[pos] *= 2  # multiplico por 2
        pos += 1


valores = [7, 2, 5, 0, 4]  # Tudo que eu fizer em lista, interfere em valores.
duplique(valores)
print(valores)

