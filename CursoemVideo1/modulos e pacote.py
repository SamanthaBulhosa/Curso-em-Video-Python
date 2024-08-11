# =================================================== MODULARIZAÇÃO  =====================================================

# surgiu no ínicio da década de 60, com a necessidade de dividir um programa já que o sistemas/código ficavam cada vez maiores,
# facilitando o aumento da legibilidade do código e entendimento de todos.

# foco: dividir um programa grande
# foco: aumentar a legibilidade
# foco: facilidade de manutenção
# ---------- VANTAGEM -------------
# ° organização do código
# ° facilidade na manutenção
# ° ocultação de código detalhado
# ° reutilização em outros projetos

# objetivo da modulos é dividir grandes problemas, em pequenas partes.

# SAMANTHA: SE VOCÊ QUISER RELEMBRAR COMO FAZER A MODULARIZAÇÃO OLHE A PASTA aprendendo modulos e pacotes ARQUIVO TEST.PY E UTEIS.PY !
"""def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


num = (int(input('Digite um valor: ')))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')"""


# =================================================== PACOTES  =====================================================

# Os modulos ajudam até certo ponto (projeto grande), já o pacote ele ajuda em projetos (extremamente grandes)
# sabendo disso podemos utilizar os pacotes para organizar cada def.

# Detro do arquivo uteis_modulos.py eu posso cria pacotes para separar por assuntos. Exemplo: (calma sam)
# Para criar um pacote eu preciso
# ir em New → escolher python package, em seguida o sistema vai criar um arquivo __int__.py
# e depois eu vou criar outro pacote que vai esta dentro de uteis_pacotes


# números
'def num():'
# string
'def nome():'
# datas
'def ano_nasc():'
# cores
'def cor():'
