# LISTA (Parte 1)

# A lista pode ser criada de 2 formas com [] ou com list[]
lista = list['hamburgue', 'cerveja', 'lasanha', 'pudim']
lanche = ['hamburgue', 'cerveja', 'lasanha', 'pudim']
print(lanche)
lanche[2] = 'picole'
print(lanche)  # com a lista eu consigo mudar a pizza para picole lista é multavel
lanche.append('biscoito')  # adiciono mais um item na lista
print(lanche)
lanche.insert(0, 'cachorro-quente')  # adiciona um item na posicao 0
print(lanche)

# -------------   Apagar elementos  ------------------

del lanche[3]  # deleta picole
lanche.pop(0)  # deleta cachorro-quente
lanche.remove('pudim')  # deleta o pudim
# todos os comandos acima deleta os elementos
print(lanche)

# como apagar um item que nao esta na lista / que nao existe
# para verificar eu preciso fazer assim:

if 'pizza' in lanche:  # a pizza esta no lanche, verifico
    lanche.remove('pizza')  # so vai remover se estiver
print(lanche)

# -----------  Criar lista atraves de range e ordem dos numeros  ----------------

valores = list(range(4, 11))  # vai 4 ate 10 e as posiçao vai 0 ate 6
print(valores)

valores = [8, 2, 5, 4, 9, 3, 2]
print(valores)  # sem ordem

valores.sort()  # em ordem do 0 até 9
print(valores)

valores.sort(reverse=True)  # em ordem so que inverso começa 9 até 0
print(valores)

# conta quantas vezes apareceu o num
print(valores.count(5))

len(valores)  # vai mostrar os números, mas ele vai contar quantidade no caso tem 7 números
print(f'essa lista tem {len(valores)} elementos')
print(valores)
# ------------------------------------------------------------------------

for v in valores:
    print(f'{v}...', end='')  # os numeros lado a lado
    # print(f'{v}...') os numeros um embaixo do outro
print('Fim do programa')

valores = list()
valores.append(4)
valores.append(9)
valores.append(0)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...', )
    # resultado para entender é esse:
    # Na posição 0 encontrei o valor 4...
    # Na posição 1 encontrei o valor 9...
    # Na posição 2 encontrei o valor 0...
print('Fim do programa')

# mostrando as posiçao pela entrada do usuario

valores = list()
for cont in range(0, 2):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!', )
print('Fim do programa')

# --------------------------------------------------
a = [2, 4, 6, 8]
b = a
b[2] = 5  # altera as 2 lista porque uma esta conectada na outra
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('=' * 20)
a = [2, 4, 6, 8]
b = a[:]  # assim eu crio uma copia de A dentro do B
b[2] = 5  # e altero o B para o num que quero sem mexer no A
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# ----------------------- NUMERO MAIOR E MENOR ----------------------------------

valor = []
maior = menor = 0
for pos in range(0, 5):
    valor.append(int(input(f'Digite um valor na posição {pos}: ')))
    if pos == 0:
        maior = menor = valor[pos]
    else:
        if valor[pos] > maior:
            maior = valor[pos]
        if valor[pos] < maior:
            menor = valor[pos]
print(f'{maior}')
print(f'{menor}')

if lista in lista.index(5):
    print(f'O valor 5 FAZ parte da lista!')
else:
    print(f'O valor 5 NÃO faz parte da lista!')
