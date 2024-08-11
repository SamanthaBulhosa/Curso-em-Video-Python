# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))  # int é para classificar como número inteiro
d = n * 2  # multiplica por 2 o numero, dobrando o valor.
t = n * 3  # multiplicar por 3 o número, triplica o valor.
r = n ** (1/2)  # exponenciação

print('O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}'.format(n, d, n, t, n, r))
print('O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}'.format(n, (n*2), n, (n*3), n, (n**(1/2))))
print('O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}'.format(n, (n*2), n, (n*3), n, pow(n, (1/2))))
# A pow()função retorna o valor de x elevado à potência de y (x y).
# \n é para quebrar a linha

# Acima temos 3 formas de fazer com que o resultado seja o mesmo.