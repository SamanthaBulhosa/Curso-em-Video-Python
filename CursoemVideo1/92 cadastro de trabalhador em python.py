# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
# de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
dados['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]  # acrescentei o elemento "sexo", para mostrar a diferença de idade entre o sexo.
dados['idade'] = datetime.now().year - ano_nasc  # ano atual - a idade
dados['ctps'] = int(input('Carteira de Trabalho (digite 0 se não tem): '))
if dados['ctps'] != 0:  # se dados['ctps'] for diferente != de 0 faça:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    if dados['sexo'] == "F":
        dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 30) - datetime.now().year)
    else:
        dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=-=' * 25)
for v, k in dados.items():
    print(f'- {v} tem o valor {k}')

# tive dificuldade para calcular o tempo de aposentadoria, mas conseguir executar o exercício sem muit

# Para homens, a idade mínima está fixada em 65 anos desde 2019. Para as mulheres,
# a idade de transição está em 62 anos desde 2023. Para ambos os sexos, o tempo mínimo
# de contribuição exigido para se aposentar 15 anos de contribuição.01/01/2024

# COMO O PROFESSOR FEZ:

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - ano_nasc  # ano atual - o ano de nascimento
dados['ctps'] = int(input('Carteira de Trabalho (digite 0 se não tem): '))
if dados['ctps'] != 0:  # se dados['ctps'] for diferente != de 0 faça:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
    # contratação + 35 = ano de contratação + 35 ano de contribuição
    # datetime.now().year  = ano atual
    # idade = recebe a soma da contratação + 35 - ano atual = que é igual aposentadoria
print('=-=' * 25)
for v, k in dados.items():
    print(f'- {v} tem o valor {k}')
