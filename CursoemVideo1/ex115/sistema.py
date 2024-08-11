# Vamos criar um menu em Python, usando modularização.
# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
# em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from ex115.biblioteca.interface import *
from ex115.biblioteca.arquivo import *
from time import sleep
# -------------------------------------- PROGRAMA PRINCIPAL --------------------------------------
arq = 'cursoemvideo.txt'  # esse é o nome do arquivo que vai ser criado ou vai procurar dentro da pasta.

if not arquivoExiste(arq):  # Se o arquivo (arq) não existir ele vai criar um com o nome que esta na variável (arq) acima:
    criarArquivo(arq)  # Crie um arquivo
# if arquivoExiste(arq):
#    print('Arquivo encontrado') se eu quiser mostrar a msg
# else:
#    print('Arquivo não encontrado') se eu quiser mostrar a msg


while True:
    resposta = menu(['\033[34mVer pessoas cadastradas\033[m',
                     '\033[34mCadastrar nova pessoa\033[m',
                     '\033[34mSair do sistema\033[m'])  # OBS: chamei meu menu([fiz uma lista, logo eu tenho um contador que vai 1 até fim dessa lista, e o item é a mensagem digitada aqui.)]
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)  # estou passando 3 parâmetros que vai esta em cadastrar
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31m ERRO! Digite uma opção válida!\033[m]')
    sleep(2)