# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

num = int(input('Digite um valor: '))
s = num + 1  # soma +1 no número digitado acima, exemplo: se eu colocar 5 em num ele add +1 e vai para 6 sendo o meu sucessor
a = num - 1  # subtrai -1 no número digitado acima, exemplo: se eu colocar 5 em num ele add -1 e vai para 4 sendo o meu antecessor
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(num, a, s))
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(num, (num - 1), (num + 1)))

# Pode ser feito de duas formas como mostra acima, porem na segunda nao utilizamos a variável.
