# Mostre uma mensagem na tela de Olá mundo

# um print a dizer olá
print('Olá, Mundo!')

# uma variável do tipo string e deverão mostrar essa variável
msg = 'Olá, Mundo'
print(msg)

# uma variável do tipo int e deverão mostrar essa variável
idade = 25
print(idade)

# uma variável do tipo float e deverão mostrar essa variável
km = float(input('Quantos Km o carro percorreu? '))
print('O carro pecorreu {}Km'.format(km))

# uma variável do tipo bool, e deverão mostrar essa variável
aceito = True
print(aceito)

# Deverão verificar cada um dos tipos e fazer print de cada um dos tipos da variável
a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print(type(msg))
print(type(idade))
print(type(km))
print(type(aceito))
print('Tem espaço?', a.isspace())
print('È um numero?', a.isnumeric())
print('È alfabetico?', a.isalpha())
print('È alfanumerico?', a.isalnum())
print('È maiúscula?', a.isupper())
print('È menúscula?', a.islower())
print('È capitalizada?', a.istitle())
