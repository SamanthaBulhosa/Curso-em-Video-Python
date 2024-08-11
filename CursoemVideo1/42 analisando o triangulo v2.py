# Refaça o DESAFIO 35 dos triângulos, acrecentando o recurso
# de mostrar que tipo de triângulo será formado:

# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

# Tive muita dificuldade de como fazer, pq tem muitas opçoes de como fazer de acordo com que o usuario vai vai fazer

# Como o PROFESSOR FEZ:

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  # Aqui eu vejo se r1 é menor que r2 e r3 e sucessivamente
    print('Os seguimentos acima PODEM FORMAR um triângulo', end=' ')
    # if r1 == r2 and r2 == r3: pode ser feito dessa forma
    if r1 == r2 == r3:  # Aqui eu estou vendo se r1 é igual a r2 e r2 é igual a r3
        print('EQUILÀTERO')
        print('TODOS os lados IGUAIS')
    elif r1 != r2 != r3 != r1:  # vejo se r1 é diferente usando != e assim sucessivamente, e coloco o r1 no final
        # para ver se r3 é igual r1
        print('ESCALENO')
        print('TODOS os lados DIFERENTE')
    else:
        print('ISÒSCLES')
        print('DOIS lados IGUAIS')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
