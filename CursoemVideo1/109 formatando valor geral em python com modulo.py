# Modifique as funções que form criadas no desafio 107 para que elas
# aceitem um parâmetro a mais, informando se o valor retornado por elas
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# # A RESOLUÇÃO DESSA ATIVIDADE ESTÁ EM OUTRA PASTA: EXERCÍCIO 107 ATÉ 115

# DEIXANDO O CÓDIGO COMPLETO AQUI (SEM MODULO) PARA VISUALIZAÇÃO DO EXERCÍCIO.

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


p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}')
