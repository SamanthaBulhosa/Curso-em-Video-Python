# Crie um programa que leia vários números inteiros pelo teclado. No final da execucao,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário, se ele quer ou nao continuar a digitar valores.

resp = 'S'
quant = soma = media = maior = menor = 0
while resp in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            menor = numero
        if numero < menor:
            menor = numero
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {:.2f}'.format(quant, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
