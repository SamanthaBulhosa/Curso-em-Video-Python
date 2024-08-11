#Crie um script python que leia o dia, o mês e o ano de nascimento
# de uma pessoa e mostre uma mensagem com a data formatada.

dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '.Correto?')  # inserir as variáveis so pelos nomes
print('Você nasceu no dia {} de {} de {}.Correto?'.format(dia, mes, ano))  # aqui usei .format com {} as chaves para
# por as datas.
