# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

a1 = float(input('Primeira nota do aluno: '))  # float é para número flutuantes que contem ponto, exemplo, peso, km
a2 = float(input('Segunda nota do aluno: '))
s = (a1 + a2) / 2  # juntei a nota a1 com a2 e depois dividir por 2 trazendo o resultado da média.
# d = s/2
print('A média entre {} e {} é igual a {}'.format(a1, a2, s))