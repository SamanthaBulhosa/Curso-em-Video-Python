# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.

def texto(msg):
    print(f'{"-" * len(msg)}')
    print(msg)
    print(f'{"-" * len(msg)}')


texto('Samantha')
texto('Curso em Video')
texto('Aprendendo Funções')


# Como sera exibido:
# --------
# Samantha
# --------
# --------------
# Curso em Video
# --------------
# ------------------
# Aprendendo Funções
# ------------------

# Conseguir fazer

# COMO O PROFESSO FEZ:
def texto(msg):
#    tam = len(msg)
    tam = len(msg) + 4  # + 4 é para colocar 2 ~ para direita e 2 ~ para a esquerda
    print('~' * tam)
    print(f'  {msg}')  # com centralização
    # print(msg)  # sem centralização do texto
    print('~' * tam)  # sem centralização do texto


texto('Samantha')
texto('Curso em Video')
texto('Aprendendo Funções')


