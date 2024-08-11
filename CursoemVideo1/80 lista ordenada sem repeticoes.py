 # Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for contador in range(0, 5):
    num = int(input('Digite um valor: '))
    if contador == 0 or num > lista[-1]:  # verifico se é o primeiro ou ultimo valor
        lista.append(num)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-=-' * 20)
print(f'Os valores digitas em ordem foram {lista}')

# esse programa ele percebe se o número começa, vai no méio ou no fim as posições

# if pos == 0: verifico se é o primeiro valor
# elif num > lista[len(lista)-1]:
# elif num > lista[-1]: (mesma coisa do de cima)
# verifico se o num é maior dentro da lista
# e o len de lista é para ver todos os elementos dentro da lista
