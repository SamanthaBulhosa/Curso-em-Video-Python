# Como  criar uma biblioteca e inserir 1 item ou mais de um item no codigo.

# import math
# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print('A raiz de {} é igual {}'.format(num, raiz))

# Acima eu importei a biblioteca matematica, e coloquei na variavel "raiz" o sqrt
# que é a raiz quadrada, que me faz fazer um calculo em raiz quadrada

# import math
# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print('A raiz de {} é igual {}'.format(num, math.ceil(raiz)))

# Acima eu consigo arredondar o valor da minha raiz quadrada, utilizando o "ceil" no print.

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual {:.2f}'.format(num, raiz))

# Acima eu só importei 1 item da biblioteca, utilizando o "from" e colocando sqrt
# que é o item, e nao precisei colocar na minha variavel "raiz" o math.sqrt pq ja foi incluido acima.
