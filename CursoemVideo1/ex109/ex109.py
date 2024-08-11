def metade(preço=0, formatar=False):
    resp = preço / 2
    return resp if not formatar else moeda(resp)


def dobro(preço=0, formatar=False):
    resp = preço * 2
    return resp if not formatar else moeda(resp)


def aumentar(preço=0, taxa=0, formatar=False):
    resp = preço + (preço * taxa) / 100
#   return resp if not formatar else moeda(resp) # if not (não vai ter formato) if formatar is falso (se formatar é falso)
    return resp if formatar is False else moeda(resp)
#   retorne resp se formatar é falso (não vai formatar) / else: senão formate preço (chamo funçao moeda(preço) para formatar)


def diminuir(preço=0, taxa=0, formatar=False):
    resp = preço - (preço * taxa) / 100
    return resp if formatar is False else moeda(resp)


def moeda(preço=0, real='R$'):  # Toda vez que chamar a função moeda vai formatar como mostra abaixo.
    return f'{real} {preço:.2f}'.replace('.', ',')  # replace vai substituir todos os '.' pontos por ',' virgula.

# Se não informar o preço, então vai receber 0
