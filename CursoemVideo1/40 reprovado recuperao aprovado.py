# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
# mensagem no final, de acordo com a média atiginda:

# Média abaixo de 5.0:
# REPROVADO

# Média entre 5.0 e 6.9:
# RECUPERAÇAO

# Média 7.0 ou superior:
# APROVADO

# Como eu fiz
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
soma = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, soma))
if soma <= 4.9:
    print('O aluno foi REPROVADO')
elif soma <= 6.9:
    print('O aluno está em RECUPERAÇÃO')
elif soma >= 7:
    print('O aluno foi APROVADO')

# Como o PROFESSOR fez:

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO')
elif média < 5:
    print('O aluno foi REPROVADO')
elif média >= 7:
    print('O aluno foi APROVADO')
