# Vamos criar um menu em Python, usando modularização.
# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
# em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

# --------------------------------------- MODULARIZAÇÃO -----------------------------------------


def cores(cor):
    colorir = (['\033[m',    # 0 - sem cores
           '\033[0;30;41m',  # 1 - vermelho
           '\033[0;30;42m',  # 2 - verde
           '\033[0;30;43m',  # 3 - amarelo
           '\033[0;30;44m',  # 4 - azul
           '\033[0;30;45m',  # 5 - roxo
           '\033[7;40m'])    # 6 - branco


def leiaInt(msg):  # ESSE TRECHO DE CÓDIGO FOI TIRADO DO EXERCÍCIO 113
    while True:  # loop infinito, vai ficar lendo até digitar um numero certo
        try:  # tente fazer isso:
            n = int(input(msg))
        except (ValueError, TypeError):  # vai verificar se é erro de valor ou tipo
            print(f'\033[31mERRO: Por favor, digite um número inteiro valido\033[m')
            continue  # faz com que volte para o loop novamente.
        except KeyboardInterrupt:  # quando o usuário força a interrupção do programa.
            print(f'\n\033[31mEntrada de dados interrompido pelo usuário.\033[m')
            #            break # para sair porque o usuário encerrou, então precisa sair, nesse caso vai mostrar o resultado none
            return 0  # se o usuário interromper vai mostrar o resultado 0
        else:
            return n


def linha(tamanho=42):  # Se eu não definir o tamanho da linha, a linha assume o tamanho 42
    return '-' * tamanho  # mostre linha- vezes* o tamanho


def cabeçalho(texto):  # esse cabeçalho foi criado para formatar o texto
    print(linha())  # chamo meu def linha para exibir aqui
    print(texto.center(42))  # mostre o texto do menu, centralize a 42 caracteres
    print(linha())


def menu(lista):  # aqui vou criar uma lista, já que vamos ter 3 opções e preciso armazenar essa informação.
    cabeçalho('MENU PRINCIPAL')  # por que o cabeçalho está aqui? porque chamo a função cabeçalho e insiro o texto já formatado.
    # Se ele não estivesse aqui eu precisaria chamar no sistema principal, cabeçalho e depois o menu.
    conte = 1  # crio um contador
    for item in lista:  # faço um laço para contar as opções
        print(f'\033[33m{conte} - {item}\033[m')  # vai haver uma contagem 1 até o tamanho da minha lista, olhar o sistema
        conte += 1
    print(linha())
    opc = leiaInt('\033[33mSua Opção: \033[m')  # chamei minha função leiaInt e coloquei uma mensagem dentro
    return opc


# ----------------------------------- MANIPULAR AQUIVOS EM PYTHON --------------------------------

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


# -------------------------------------- PROGRAMA PRINCIPAL --------------------------------------

arq = 'cursoemvideo.txt'  # esse é o nome do arquivo que vai ser criado ou vai procurar dentro da pasta.

if not arquivoExiste(arq):  # Se o arquivo (arq) não existir ele vai criar um com o nome que esta na variável (arq) acima:
    criarArquivo(arq)  # Crie um arquivo

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
