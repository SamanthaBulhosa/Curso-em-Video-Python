n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
e = n1**n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1 % n2
a = n1+n2
s = n1-n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))

# end = ' ' faz com que o print abaixo continue na mesma linha
# \n faz com que o codigo quebre em qualquer parte pulado para proxima linha
