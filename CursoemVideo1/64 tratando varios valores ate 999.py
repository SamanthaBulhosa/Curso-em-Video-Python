# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuario digitar o valor 999, que é a condiçao de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsidere o flag).
# Obs: o flag é o 999 que é o comando de parada!

# Fiz sozinha
num = 0   # Como fazer de forma simples:
cont = 0  # para simplificar já que todos levam o valor de zero posso fazer assim:
soma = 0  # num = cont = soma = 0
while num < 999:
    num = int(input('Digite um número [999 para parar]: '))
    cont += 1
    soma += num
    num += soma
soma -= 999  # Não é para fazer assim, pq minha variavel esta com valor errado -999
# e é consideravel gambiarra
cont -= 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

# Como o PROFESSOR fez:
num = cont = soma = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

# Obs: também não é para colocar a pergunta 2 vez,
# como mostra acima, uma fora do while e outra dentro do while.
# Exercicio 65 mostra como fazer melhor esse projeto
