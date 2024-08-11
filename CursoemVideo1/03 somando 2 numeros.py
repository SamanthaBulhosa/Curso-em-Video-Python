# Crie um script python que leia dois números e tente mostrar a soma entre eles.

n1 = int(input('Digite um número = '))
n2 = int(input('Digite mais um número = '))
s = n1 + n2  # soma o n1 com n2 mostrando o resultado dessa junção

print('A soma vale', s)  # mostra a frase e a soma dos 2 valores digitados.
print('A soma entre', n1, 'e', n2, 'vale', s)  # aqui mostra a frase, os 2 números digitados e a soma
print('A soma entre {} e {} vale {}'.format(n1, n2, s))  # aqui usei o .format e traz o mesmo resultado do print acima
