# Faça um programa que leia a largula e a altura de uma parede em metros , calcule a
# sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de
# tinta pinta uma área de 2m².

l = float(input('Qual a largura da parede: '))
a = float(input('Qual a altura da parede: '))
area = l * a
t = area / 2
print('A sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede,'
      ' você precisa de {}L de tinta.'.format(l, a, area, t))