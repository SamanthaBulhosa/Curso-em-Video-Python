for c in range(1, 6):  # aparece meu nome 5 vez se eu quiser ate 6 tem que (0, 7)
    print('Samantha')

for conte in range(0, 6):  # aparece o numero de 0 a 5
    print(conte)
print('Fim')

for conte in range(6, 0, - 1):  # para contar de trás para frente 6 ate 1
    print(conte)
print('FIM')

for pule in range(0, 7, 2):  # pula em 2 em 2 ate chegar no fim
    print(pule)
print('FIMM')

n = int(input('Digite um número: '))
for c in range(0, n + 1):  # vai conta do numero inserido acima ate o fim
    # foi colocado +1 para ir ate o 5 se nao colocar vai ate o 4
    print(c)
print('Fim')

for repita in range(0, 3):  # O usuario vai digitar 3 vezes o valor
    num = int(input('Digite um valor: '))
print('Fimmmm')

somar = 0  # aqui eu consigo somar o valor digitado pelo usuario ex: 4, 8, 3, 1 o total é 16
for pergunte in range(0, 4):
    num = int(input('Digite um valor: '))
    somar += num
print('O somatório de todos os valores foi {}'.format(somar))

