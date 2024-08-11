# Vamos criar um menu em Python, usando modularização.
# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
# em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

# ------------------------------------- MODULARIZAÇÃO -----------------------------------------
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