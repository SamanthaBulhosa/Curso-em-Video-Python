# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

cores = ('\033[m',  # 0 - sem cores
         '\033[0;30;41m',  # 1 - vermelho
         '\033[0;30;42m',  # 2 - verde
         '\033[0;30;43m',  # 3 - amarelo
         '\033[0;30;44m',  # 4 - azul
         '\033[0;30;45m',  # 5 - roxo
         '\033[7;40m'  # 6 - branco
         )


def ajuda(comd):
    titulo(f'Acessando o manual do comando \'{comd}\'', 5)  # cor 5 é a roxa, comd é o nome que o usuário digitou
    print(cores[6], end='')  # pinto da cor 6 que é branco e vai exibir a msg, logo abaixo tiro a cor
    help(comd)
    print(cores[0], end='')  # tirei a cor aqui para não dar continuidade a próxima mensagem com cor branca.


def titulo(msg, cor=0):
    tamanho_texto = len(msg) + 4  # O '+4' é para colocar mais quatro traços no ínicio e fim do texto.
    print(cores[cor], end='')
    print('-' * tamanho_texto)
    print(f' {msg}')
    print('-' * tamanho_texto)
    print(cores[0], end='')


# Programa principal:
comando = ''  # comando recebe '' str vazia
while True:  # enquanto for verdade faça:
    print(cores[3], 'SISTEMA DE AJUDA PyHELP', cores[0])
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':  # Meu comando contem o método '.upper' que joga as letras para maiúsculo,
        # se for igual a 'fim' o programa encerra porque deixa de ser verdade e passa a ser False.
        break
    else:
        ajuda(comando)  # interligo o comandando digitado pelo usuário com a ajuda que está no def acima.
print(cores[1], 'ATÉ LOGO')
