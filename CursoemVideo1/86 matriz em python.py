# Crie um programa que crie uma matriz de dimensão 3x3 e preencha os valore lidos pelo teclado
# No final, mostre a matriz na tela com a formatação correta.

"""num = []
for valor in range(0, 3):
    num.append(int(input(f'Digite um valor para {valor, valor}: ')))
    num.append(int(input(f'Digite um valor para {valor, valor+1}: ')))
    num.append(int(input(f'Digite um valor para {valor, valor+2}: ')))
    num.append(int(input(f'Digite um valor para {valor, valor+3}: ')))
print('=-=' * 25)
print(num)"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # uma lista e dentro tenho sublist, no total eu tenho 9 zeros dentro da lista por isso no meu range nao precisei colocar 0 a 9
for linha in range(0, 3):  # aqui eu entendo que para cada sublist posso inserir 3 números
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha, coluna}: '))
print('=*=' * 20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')  # OBS: aqui eu vou mostrar cada linha exemplo: [1] [2] [3],
        # testei no exercício 87 sem essa linha de código e no print so exibia o ultímo numero da lista, exemplo [6]
        # :^5 isso faz com que eu deixe centralizado e organizado os números com os espaços
    print()  # sem esse print nao pularia a linha
