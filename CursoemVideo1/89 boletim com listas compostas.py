# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

alunos = []
dados = []
while True:  # loop infinito
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    resp = str(input('Quer Continuar? [S/N]: ')).upper().strip()[0]
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])  # lista composta é feito assim
    if resp == 'N':
        break
print('-' * 30)
print(f'{"NOME":<15} {"MÉDIA":>8}')
print('-' * 30)
# dificuldade em mostrar os nomes e media
for i, a in enumerate(
        alunos):  # 'i' é índice que vai enumerar, o 'a' é onde vou mostrar os nome, e media usando '[0]' para mostrar dentro da lista qual dado quero exibir ex: a[2] é a média.
    print(f'{i:>3}{a[0].upper():>5}{a[2]:>8}')  # o ':>3' é para criar espaços
while True:
    print('_' * 35)
    nota_geral = int(input(f'Mostrar a nota de qual aluno? (999 para interromper): '))
    if nota_geral == 999:
        print('FINALIZANDO...')
        break
    if nota_geral <= len(alunos) - 1:  # se for menor do que len mostra as notas
        print(f'Notas de {alunos[nota_geral][0]} são {alunos[nota_geral][1]}')
#   if nota_geral >= len(alunos):
#        print(f'A lista de alunos é {len.alunos}')
print('<<< VOLTE SEMPRE >>>')


#  A função len em Python é uma função embutida que retorna o número
#  de elemento em um objeto. Ela pode ser usada para contar o número de itens em uma lista,
#  o número de caracteres em uma string, o número de chaves em um dicionário, entre outros.
#  A sintaxe básica para usar a função len é escrever “len(objeto)”.