# Um Script que faça um ciclo for que vá de 0 a 100
for conte in range(0, 101):
    print(conte)
print('Fim do programa de 0 ate 100')
# Um Script que faça um ciclo for que vá de 5 a 105
for conte in range(5, 106):
    print(conte)
print('Fim do programa de 5 ate 105')
# Um Script que percorra todos os números entre 0 e 50 e mostre a soma de todos esses números
soma = 0
for conte in range(0, 51):
    print(conte)
    soma += 1
print('A soma de todos os números são {}'.format(soma))
print('Fim do programa de 0 ate 50')
'''o meu conta ate 51, nao sei como faço para desconsiderar o 0 (zero).'''
# Um Script que faça um ciclo for que vá de 100 a 0
for cont in range(100, -1, -1):
    print(cont)
print('Fim do programa de 100 ate 0')
# Um Script que mostre todos os números divisíveis por 3, entre 1 e 1000
for cont in range(1, 1000):
    if cont % 3 == 0:
        print(cont)
# Um Script que percorra uma string e mostre todas as letras da string
nome = str(input('Qual o seu nome? '))
for letras in nome:
    print(letras)
print('Fim do programa exibindo a str nome')
# Um Script que percorra uma string e mostre quantas vezes uma letra se repete
soma = 0
nome = str(input('Qual o seu nome? '))
edit = nome.upper().strip()
for letras in nome:
    if letras == 'a':
        soma += 1
    print(letras, end='')
print('\n aparece a letra "A" {}x'.format(soma))
print('Fim do programa exibindo os caracteres da letra "A"')

