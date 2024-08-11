# Adapte o código do desafio 107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

# A RESOLUÇÃO DESSA ATIVIDADE ESTÁ EM OUTRA PASTA: EXERCÍCIO 107 ATÉ 115

# DEIXANDO O CÓDIGO COMPLETO AQUI (SEM MODULO) PARA VISUALIZAÇÃO DO EXERCÍCIO.

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


def moeda(preço=0, real='R$'):  # Toda vez que chamar a função moeda vai formatar como mostra abaixo.
    return f'{real} {preço:.2f}'.replace('.', ',')  # replace vai substituir todos os '.' pontos por ',' virgula.

# Se não informar o preço, então vai receber 0


p = float(input('Digite o preço: R$'))
# print(f'A metade de {p:.2f} é {ex108.metade(p)}')  utilizando o :.2f consigo formatar, mas fica limitado
print(f'A metade de {moeda(p)} é {metade(p)}')  # tudo que eu quiser formatar precisa está dentro (ex108.)
print(f'O dobro de {moeda(p)} é {dobro(p)}')
print(f'Aumentando 10%, temos {aumentar(p, 10)}')
print(f'Diminuindo 13%, temos {diminuir(p, 13)}')
