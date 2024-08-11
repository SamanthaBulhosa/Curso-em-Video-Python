# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = str(input('Nome: '))
media = float(input(f'Média de {aluno}: '))
print('=-=' * 15)
print(f'- Nome é igual a {aluno}')
print(f'- Média é igual a {media}')
if media >= 7:
    print(f'Situação é igual a Aprovado')
elif 5 <= media < 7:
    print(f'Situação é igual a Recuperação')
elif media < 5:
    print(f'Situação é igual a Reprovado')

# Nesse execício nao precisei usar o dicionário, o que o professor
# propôs a fazer era algo simples onde nao vejo a necessidade de usar.

# usei com o dicionario
dados = dict()
dados['aluno'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["aluno"]}: '))
print('=-=' * 15)
print(f'- Nome é igual {dados["aluno"]}')
print(f'- Média é igual a {dados["media"]}')
if media >= 7:
    print(f'Situação é igual a Aprovado')
elif 5 <= media > 7:
    print(f'Situação é igual a Recuperação')
elif media < 5:
    print(f'Situação é igual a Reprovado')
print(dados)  # para mostrar que está guardado em um dicionário.

# COMO O PROFESSOR FEZ:

dados = dict()
dados['aluno'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["aluno"]}: '))
print(f'- Nome é igual {dados["aluno"]}')
print(f'- Média é igual a {dados["media"]}')
if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
print('=-=' * 15)
for k, v in dados.items():
    print(f'{k} é igual a {v}')
print('=-=' * 15)