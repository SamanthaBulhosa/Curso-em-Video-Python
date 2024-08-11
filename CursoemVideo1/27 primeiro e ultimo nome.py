# Faça um programa que leia o nome completo de uma pessoa, mostrando em
# seguida o primeiro e o ultimo nome separado

# Ex: Ana Maria de Souza
# Primeiro: Ana
# Ultimo: Souza

n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))

# Nao entendi muito bem esse exercicio e achei difícil!
