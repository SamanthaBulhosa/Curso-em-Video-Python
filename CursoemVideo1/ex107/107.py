# Crie um módulo chamado test108.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
# e use algumas dessas funções.

"""import ex107

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {ex107.metade(p)}')
print(f'O dobro de {p} é {ex107.dobro(p)}')
print(f'Aumentando 10%, temos {ex107.aumentar(p)}')
print(f'Diminuindo 13%, temos {ex107.diminuir(p)}')"""

# O exercício precisa está dentro da mesma pasta que o meu modulo para fazer a importação.
# Se criei um arquivo 107 na pasta 'venv' e criar o modulo 'ex_preço' em outra pasta fora
# do 'venv' não consigo importa as informações, e acaba me gerando um erro.

# COMO O PROFESSOR FEZ:

import ex107  # importando toda a biblioteca

# Lembrando que se eu fizer desse jeito preciso tirar ex107. e colocar so o nome da função

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {ex107.metade(p)}')
print(f'O dobro de {p} é {ex107.dobro(p)}')
print(f'Aumentando 10%, temos {ex107.aumentar(p, 10)}')   # importo a biblioteca ex107., nomes das funções, mais os 2 parâmetros.
print(f'Diminuindo 13%, temos {ex107.diminuir(p, 13)}')

# no meu não tem o parâmetro taxa, então o meu resultado vai direto
# como o professor criou o segundo parâmetro se eu nao colocar o valor '10'
# gera um erro.