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


def resumo(preço=0, taxa_aumento=10, taxa_diminuir=5):
    print('--' * 15)
    print('RESUMO DO VALOR'.center(30))  # o .center(30) é para centralizar o texto com espaço de 30
    print('--' * 15)
    print(
        f'Preço analisado: \t{moeda(preço)}')  # O \t é uma tabulação que faz uma tabela e deixa organizado ao exibir com espaçamento
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'{taxa_aumento}%, de temos \t\t{aumentar(preço, taxa_aumento, True)}')
    print(f'{taxa_diminuir}%, de temos \t\t{diminuir(preço, taxa_diminuir, True)}')
