# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas
# pessoas ainda nao atingiram a maioridade e quantas já sao maiores.

from datetime import date
ano_atual = date.today().year
cont_maiores = 0
cont_menores = 0
for ano in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(ano)))
    idade = ano_atual - nasc
    if idade >= 21:
        cont_maiores += 1
    else:
        cont_menores += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont_maiores))
print('E também tivemos {} pessoas menores de idade'.format(cont_menores))

