# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:

# A media de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_homem_velho = 0
menos_20anos = 0
for pessoa in range(1, 5):
    print('----- {}° PESSOA -----'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip()
    soma_idade += idade
    media_idade = soma_idade / 4
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        menos_20anos += 1
print('A média de idade do grupo é de {:.2f} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_homem_velho))
print('Ao todo são {} mulhere com menos de 20 anos.'.format(menos_20anos))
