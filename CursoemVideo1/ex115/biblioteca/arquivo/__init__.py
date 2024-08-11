# Vamos criar um menu em Python, usando modularização.
# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
# em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.


# ----------------------------------- MANIPULAR AQUIVOS EM PYTHON --------------------------------
from ex115.biblioteca.interface import *


# VERIFICA SE O ARQUIVO EXISTE
def arquivoExiste(nome):
    try:  # Se eu (try/tentou) abrir o arquivo do código abaixo, esta OK e não cai no except, caso nao abra ele cai no except e mostra o erro
        arquivo = open(nome,
                       'rt')  # abra/open - arquivo/nome(é o arq que está interligado no arquivoExiste) - leitura de texto/rt
        arquivo.close()
    except FileNotFoundError:  # Essa é uma (exceção/except) Se o (arquivo não foi encontrado/FileNotFoundError)
        return False
    else:
        return True


# CRIA O ARQUIVO
def criarArquivo(nome):
    try:
        arquivo = open(nome,
                       'wt+')  # abra/open - arquivo/nome (é o arq que está interligado no criarArquivo(arq) - gravação de texto/wt e o + é que faz a magíca de criar o arquivo.
        arquivo.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Aquivo {nome} criado com sucesso!')


# LEITURA DO ARQUIVO JÁ EXISTENTE
def lerArquivo(nome):
    try:  # tentei abrir
        arquivo = open(nome, 'rt')  # rt/ ler texto)
    except:  # se der error
        print('Erro ao ler o arquivo!')
    else:  # se não der error
        cabeçalho('PESSOAS CADASTRADAS')
        for informacao in arquivo:  # para cada informacao dentro de arquivo, faça: (o 'arquivo' é o que está acima em try!
            dado = informacao.split(';')
            dado[1] = dado[1].replace('\n', '')  # tenho um \n que pula a linha, precisei colocar replace aqui para substituir \n por nada ''
            print(f'{dado[0]:<30}{dado[1]:>3} anos')  # dados[0]:recebe <esquerada 30caracteres / dado[1]:recebe >direita 3caracteres
    #    print(arquivo.read())  # read ler tudo que esta no arquivo e sem lista
    #    print(arquivo.readlines())  # o readlines ele pega as linhas de um arquivo e faz uma lista,
    #    exemplo: ['Samantha\n', 'yasmim\n', 'paloma\n']
    finally:  # dando certo ou errado o programa vai ser fechado
        arquivo.close()


# CADASTRAR DADOS PARA DENTRO DE UM ARQUIVO
def cadastrar(arq, nome='desconhecido(a)', idade=0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo.')
    else:
        try:  # posso colocar uma dentro de outro.
            arquivo.write(f'{nome};{idade}\n')  # .write é para escrever
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            arquivo.close()
