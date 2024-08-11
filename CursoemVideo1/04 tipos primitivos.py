# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ela.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))  # usando o type eu descubro o tipo de dado, como int, float ou str.
print('Tem espaço?', a.isspace())
print('È um numero?', a.isnumeric())
print('È alfabético?', a.isalpha())
print('È alfanúmerico?', a.isalnum())
print('È maiúscula?', a.isupper())
print('È minúscula?', a.islower())
print('È capitalizada?', a.istitle())  # Capitalizado utiliza letras maiúsculas para cada palavra, sem espaços ou sublinhados.
