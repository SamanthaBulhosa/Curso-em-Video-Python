# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for impar, desconsidere-o

total = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    soma = num % 2
    if soma == 0:
        total += num
    if num == 1:
        print('Desconsidere')
print('A soma total dos valores PARES acima é {}'.format(total))

# CONSEGUIR SOZINHA, esse foi dificio, estava errando a ordem das vareaveis, colocando no lugar errado
# Fiz errado, o do professor esta diferente pq mostra quantos numero pares e o total

# Como o PROFESSOR FEZ:

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num
print('Você informou {} número PARES e a soma foi {}'.format(cont,soma))

