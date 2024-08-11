# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.

lista = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:  # se num nao estiver em lista
        lista.append(num)  # adicione em lista o num (TRADUÇÃO DA LINHA 10 E 11)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')

# Nao conseguir apagar os valores iguais! dificuldade...

