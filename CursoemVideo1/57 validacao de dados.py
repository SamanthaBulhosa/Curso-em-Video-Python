# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitacao novamente até ter um valor correto.

sexo = str(input('Informe seu sexo:[M/F] ')).strip().upper()[0]  # tirei os espaços e coloquei em maiuscula e fiz o
# fatiamento que mesmo que a pessoa digite outra coisa so vai sair a primeira letra.
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
