# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
# com a mesma funcionalidade.

def leiaInt(msg):
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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número real valido\033[m')
            continue
        except KeyboardInterrupt:  # quando o usuário força a interrupção do programa.
            print(f'\n\033[31mEntrada de dados interrompido pelo usuário.\033[m')
            return 0
        else:
            return n


num1 = leiaInt('Digite um número Inteiro: ')
num2 = leiaFloat('Digite um número Real: ')
print(f'Você acabou de digitar o número inteiro {num1} e o real {num2}')
