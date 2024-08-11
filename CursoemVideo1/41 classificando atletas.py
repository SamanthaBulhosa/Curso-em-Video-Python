# A Confederação Nascional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MESTER

from datetime import date

nasc = int(input('Ano de Nascimento: '))
ano = date.today().year - nasc  # Ano atual - nasc (ex: 2023 - 1997 = 26 anos)
print('O atleta tem {} anos.'.format(ano))
if ano <= 9:
    print('Classificação: MIRIM')
elif ano <= 14:
    print('Classificação: INFANTIL')
elif ano <= 19:
    print('Classificação: JUNIOR')
elif ano <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MESTER')
# Conseguir sozinhaa

# Como o PROFESSOR FEZ:

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if ano <= 9:
    print('Classificação: MIRIM')
elif ano <= 14:
    print('Classificação: INFANTIL')
elif ano <= 19:
    print('Classificação: JUNIOR')
elif ano <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MESTER')
