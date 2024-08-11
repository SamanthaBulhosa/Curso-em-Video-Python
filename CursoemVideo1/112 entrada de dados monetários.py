# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

# ESSE EXERCÍCIO É PARA FAZER COM PACOTE, MAS COLOQUEI AQUI A RESOLUÇÃO TODA E CONSIGO EXECUTAR.

# from utilidadesexterno import moedapacote
# from utilidadesexterno import dadospacote

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
def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()  # replace: substitui todas as ,virgulas por .ponto
        if entrada.isalpha() or entrada == '':
            # if entrada.isalpha() or entrada.strip() == '':
            # Se a entrada for isalpha que é (alfanumérico / letra e número).
            # OU entrada for strip que é (vazio '' ou cheia de espaço)
            print(f'\033[031mERRO: \"{entrada}\" é um preço invalido!\033[m')
        else:
            valido = True
            return float(entrada)

# p = float(input('Digite o preço: R$')) Altero essa linha para a de baixo ja que estou
p = leia_dinheiro('Digite o preço: R$')  # vai me retornar como um input so que fazendo uma verificação
resumo(p, 35, 22)