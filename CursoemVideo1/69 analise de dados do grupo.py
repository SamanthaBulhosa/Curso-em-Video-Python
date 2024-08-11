# Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuario
# quer ou nao continuar. No final, mostre:

# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

mais18 = quant_sexoM = quant_sexoF = 0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        quant_sexoM += 1
    if sexo == 'F' and idade < 20:
        quant_sexoF += 1
    contin = ' '
    while contin not in 'SN':
        contin = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if contin == 'N':
        break
print('==== FIM DO PROGRAMA ====')
print(f'Total de pessoas com mais de 18 anos: {mais18} \n'
      f'Ao todo temos {quant_sexoM} homens cadastrados \n'
      f'E temos {quant_sexoF} mulheres com menos de 20 anos')

# OBS: difiuldade para verificar dados, ex: acima se o usurio digitar qualquer outra letra
# sem ser F/M vai continuar com o programa sem repetir que ele digitou errado!
