# Crie um módulo chamado test108.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
# e use algumas dessas funções.


# A RESOLUÇÃO DESSA ATIVIDADE ESTÁ EM OUTRA PASTA: EXERCÍCIO 107 ATÉ 115
# DEIXANDO O CÓDIGO COMPLETO AQUI (SEM MODULO) PARA VISUALIZAÇÃO DO EXERCÍCIO.

def metade(preço):
    resp = preço / 2
    return resp


def dobro(preço):
    resp = preço * 2
    return resp


def aumentar(preço, taxa):  # esse preço e taxa não são os mesmo de parâmetro diminuir, ja que está em um escopo local.
    resp = preço + (preço * taxa) / 100
    return resp


def diminuir(preço, taxa):
    resp = preço - (preço * taxa) / 100
    return resp

# OBS: em como eu fiz, não coloquei uma variável 'resp' porque achei que não iria precisa, mas o professor falou
# que iriamos usar essa 'resp' nos próximos exercício fazendo assim eu ter esse resultando de 'resp' em outro arquivo.

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10%, temos {aumentar(p, 10)}')
print(f'Diminuindo 13%, temos {diminuir(p, 13)}')
