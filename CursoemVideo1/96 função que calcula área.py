# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno

def area(largura, comprimento):
    tamanho = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {tamanho}m2')


print('Controle de Terrenos')
print('---' * 10)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)  # aqui eu estou informando para area que o valor em 'l' e 'c' vai ser inserido em largura e comprimento

# NAO CONSEGUIR FAZER ESSE EXERCÍCIO
