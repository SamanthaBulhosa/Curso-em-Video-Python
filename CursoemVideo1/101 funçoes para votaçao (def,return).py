# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# COMO EU FIZ:
from datetime import datetime


def voto(ano_nasc):
    ano = datetime.now().year - ano_nasc
    print(f'Com {ano} anos: ', end='')
    if ano <= 16:
        print('VOTO NEGADO')
    elif ano == 17:
        print('VOTO OPCIONAL')
    elif ano < 65:
        print('VOTO OBRIGATÓRIO')
    elif ano >= 65:
        print('VOTO OPCIONAL POR IDADE')


print('-=-' * 15)
voto(int(input('Em que ano você nasceu? ')))

# COMO O PROFESSOR FEZ:


def voto(ano):
    from datetime import date  # quando eu importo uma biblioteca para detro de uma função, ela se torna local e so serve para dentro dela,
    # outra vantagem disso é que eu economizo memória, porque a class 'date' vai ficar na memória durante a execução desse trecho de código
    atual_ano = date.today().year
    idade = atual_ano - ano
    if idade < 16:  # Se idade for menor que 16, então faça:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:  # Se idade for igual a 16 e menor que 18 OU idade for maior que 65, então faça:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:  # Se a idade nao se enquadra em: menor ou igual a 16,18 e maior que 65, então faça:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa principal:
ano_nasc = int(input('Digite o ano de nascimento: '))
print(voto(ano_nasc))  # O 'voto' recebe 'ano_nasc' que interligo com o def 'ano' como parâmetro.
