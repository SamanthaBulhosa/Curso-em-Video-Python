# COMO EU FIZ:

""" def metade(preço):
    return preço / 2


def dobro(preço):
    return preço * 2


def aumentar(preço):
    porcentagem = 10
    soma = (preço * porcentagem) / 100
    return soma + preço


def diminuir(preço):
    porcentagem = 13
    soma = (preço * porcentagem) / 100
    return preço - soma"""

# COMO O PROFESSOR FEZ:


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