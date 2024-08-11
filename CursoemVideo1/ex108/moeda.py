def metade(preço=0):
    resp = preço / 2
    return resp


def dobro(preço=0):
    resp = preço * 2
    return resp


def aumentar(preço=0,
             taxa=0):  # esse preço e taxa não são os mesmo de parâmetro diminuir, ja que está em um escopo local.
    resp = preço + (preço * taxa) / 100
    return resp


def diminuir(preço=0, taxa=0):
    resp = preço - (preço * taxa) / 100
    return resp


def moedas(preço=0, moeda='R$'):  # Toda vez que chamar a função moeda vai formatar como mostra abaixo.
    return f'{moeda} {preço:.2f}'.replace('.', ',')  # replace vai substituir todos os '.' pontos por ',' virgula.

# Se não informar o preço, então vai receber 0
