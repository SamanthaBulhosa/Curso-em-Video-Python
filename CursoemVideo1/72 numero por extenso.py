# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
          'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
          'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Voce digitou o número {numero[num]}')
    print('Tente novamente...', end='')
print('FIM')

# CONSEGUIR SOZINHA, DEMOROU PARA ENTENDER, MAS FOI!!!
# No meu codigo acima se eu digitar -1 vai dar o resultado vinte.

# Como o PROFESSOR FEZ:

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete'
        , 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze'
          , 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    continuar = ' '
    if 0 <= num <= 20:
        print(f'Voce digitou o número {cont[num]}')
        if continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
            if continuar == 'N':
                break
print('FIM DO PROGRAMA! ')