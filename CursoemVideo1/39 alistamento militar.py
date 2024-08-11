# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# - Se ele ainda vai se alista ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o campo que falta ou que possou do prazo

# Como o PROFESSOR fez:

from datetime import date
print('''Escolha abaixo o seu sexo
[ 1 ] MASCULINO
[ 2 ] FEMENINO ''')
sexo = int(input('Qual o seu sexo: '))
if sexo == 2:
    print('O sexo FEMENINO não precisa fazer alistamento militar obrigatório.')
elif sexo == 1:
    print('Seguindo com o seu alistamento...')
    nasc = int(input('Ano de nascimento: '))
    ano_atual = date.today().year
    idade_usuario = ano_atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade_usuario, ano_atual))
    if idade_usuario == 18:
        print('Você tem que se alistar IMEDIATAMENTE')
    elif idade_usuario < 18:
        tempo = 18 - idade_usuario
        ano = ano_atual + tempo
        print('Ainda falta {} anos para o alistamento'.format(tempo))
        print('Seu alistamento será em {}.'.format(ano))
    elif idade_usuario > 18:  # Poderia usar o else mas fica mais claro o entendimento assim.
        tempo = idade_usuario - 18
        ano = ano_atual - tempo
    #   ano = date.today().year - tempo
        print('Você já deveria ter se alistado há {} anos atrás.'.format(tempo))
        print('Seu alistamento foi em {}.'.format(ano))