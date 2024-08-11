# TEXTANDO AS CONDIÇOES

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua nota foi {}'.format(m))
if m >= 6:
    print('PARABÈNS')
else:
    print('ESTUDE MAIS')

# CONDIÇAO

nome = input('Qual é o seu nome: ')
if nome == 'Samantha':
    print('Esse é o nome mais lindo do mundo')
print('Bom dia {}'.format(nome))

# CONDIÇAO COMPOSTA

tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('---FIM---')

# CONDIÇÕES SIMPLIFICADAS

tempo = int(input('Quanto anos tem o seu carro? '))
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('---FIM---')