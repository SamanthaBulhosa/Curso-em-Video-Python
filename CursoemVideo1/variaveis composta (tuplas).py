# lanche = (tupla) [lista] {dicionario}
# Tuplas sao IMUTAVEIS, nao muda

lanche = ('Hamburgue', 'Suco', 'Pizza', 'Pudim')  # posso fazer sem parenteses ()
print(lanche[2])

# O CODIGO ABAIXO EU USO O RANGE
for comida in lanche:  # Faz um laço se repetido a frase e mudando os nomes dos lanches
    print(f'Eu vou comer {comida}')
print(f'Comi muito!')

# O CODIGO ABAIXO EU USO A VARIAVEL COMPOSTA
lanche = ('Hamburgue', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    # print(lanche[cont])
    print(f'Eu vou comer {lanche[cont]}')
print(f'Comi muito!')

# DUAS FORMAS DE INUMERAR AS POSIÇOES DOS ITENS:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')  # aqui eu consigo ver os numeros de cada item

# OUTRA MANEIRA DE ENUMERAR!
for pos in enumerate(lanche):
    print(f'Eu vou comer {lanche} na posicao {pos}')

print('{:-^55}'.format(''))
print((sorted(lanche)))  # Organiza em ordem alfabetica
# Os 2 da o mesmo resultado! so que muda sao as tecnicas de fazer.

# -------------------------------------------------------------------------------

a = (2, 5, 6, 8)
b = (1, 3, 4, 7)
c = a + b
print(c)  # junta A e o B mostrando os numeros
print(c.count(5))  # conta quantas vezes apareceu o 5 entre o A e o B, que no caso 1 vez
print(c.index(8))  # mostra a posicao, exempro o 8 esta na posicao 3

pessoa = ('Samantha', 26, 'F', 40.00)
print(pessoa)  # Posso ter dados de diferentes tipos
del pessoa  # Deleta a informaçao acima toda, nao deixando gravado em lugar nenhum!
print(pessoa)  # Da erro porque usei o comado del para apagar, e nao acha o dado acima.

