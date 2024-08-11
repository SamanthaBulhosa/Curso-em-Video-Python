from moeda import *  # O * chama todas as funções sem precisar utilizar o nome da pasta,
# exemplo: moeda.dobro que é o que o import moeda faz

p = float(input('Digite o valor: '))
print(f'A metade de {moedas(p)} é {moedas(metade(p))}')
print(f'O dobro de {moedas(p)} é {moedas(dobro(p))}')
print(f'Aumentando 10%, temos {moedas(aumentar(p, 10))}')
print(f'Diminuendo 13%, temos {moedas(diminuir(p, 13))}')

# O professor fez 3 arquivos com o nome moeda, só que ficou tudo confuso,
# fazendo com que eu não entendesse e não conseguisse ligar os pontos.
# Procurei outra forma de refazer o exercício e que rodasse esse código.

#   1     2   5
# MOEDA.MOEDA(P)
#   1     2     3     4    5
# MOEDA.MOEDA(MOEDA.METADE(P)
'1 - nome do modulo'
'2 - nome da função'
'3 - nome do parâmetro'



