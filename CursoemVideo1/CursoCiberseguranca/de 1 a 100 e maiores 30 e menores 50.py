# Fazer um ciclo que percorra os numeros entre 1 e 100,
# mas mostre apenas os que são maiores do que 30 e menores do que 50

num = 1
while num <= 100:
    if num <= 30 or num >= 50:
        print(num)
    num += 1
print('FIM')