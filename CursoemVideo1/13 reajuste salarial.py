# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

s = float(input('Qual o salario do funcionario? R$'))
n = s + (s * 15 / 100)
print('Um funcionario que ganhava{:.2f}, com 15% de aumento, passa a receber {:.2f}'.format(s, n))
