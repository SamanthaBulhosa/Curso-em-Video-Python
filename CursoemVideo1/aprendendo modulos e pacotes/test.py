# ==================================== MODULOS ============================================================

"""import uteis_modulos  # eu estou importando o arquivo que criei em uteis para esse arquivo.

num = (int(input('Digite um valor: ')))
fat = uteis_modulos.fatorial(num)  # preciso colocar o .uteis
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis_modulos.dobro(num)}')
print(f'O triplo de {num} é {uteis_modulos.triplo(num)}')

# meu programa funciona normalmente, so que de forma simplificada.

# OUTRA FORMA DE IMPORTA:

from uteis_modulos import fatorial, dobro, triplo  # eu estou importando o arquivo porem somente com a função

# OBS IMPORTANTE: não é muito recomendando utilizar dessa forma, porque pode ter conflitos com outra
# biblioteca que tenha o mesmo nome que a minha função declara, e entrar em um conflito de 'qual biblioteca executar?'
# e pode me retornar um resultado oposto do que desejo (na prática a que vale é ultima biblioteca importada.)

num = (int(input('Digite um valor: ')))
fat = fatorial(
    num)  # nao preciso colocar '.uteis' a frente como o exemplo mostrado acima, devido a minha chamada no import
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')"""

# ======================================== PACOTES ============================================================

from uteis_pacote import numero  # eu estou importando o arquivo que criei em uteis para esse arquivo.

num = (int(input('Digite um valor: ')))
fat = numero.fatorial(num)  # preciso colocar o .uteis
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numero.dobro(num)}')
print(f'O triplo de {num} é {numero.triplo(num)}')

# meu programa funciona normalmente, so que de forma simplificada.

# OUTRA FORMA DE IMPORTA:

from uteis_pacote import datas, numero, string  # eu estou importando o arquivo porem somente com a função

# OBS IMPORTANTE: não é muito recomendando utilizar dessa forma, porque pode ter conflitos com outra
# biblioteca que tenha o mesmo nome que a minha função declara, e entrar em um conflito de 'qual biblioteca executar?'
# e pode me retornar um resultado oposto do que desejo (na prática a que vale é ultima biblioteca importada.)

num = (int(input('Digite um valor: ')))
fat = fatorial(num)  # nao preciso colocar '.uteis' a frente como o exemplo mostrado acima, devido a minha chamada no import
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')