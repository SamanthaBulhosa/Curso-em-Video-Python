# Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento
# Para salário superior a R$1.250,00 calcule um aumento de 10%
# E para os inferiores ou iguais o aumento é de 15%

# COMO EU FIZ
s = float(input('Qual o salário do funcionario? R$'))
a15 = s + (s * 15 / 100)
a10 = s + (s * 10 / 100)
if s <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.3f} agora.'.format(s, a15))
if s > 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.3f} agora.'.format(s, a10))

# COMO O PROF FEZ
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.3f} agora.'.format(salario, novo))