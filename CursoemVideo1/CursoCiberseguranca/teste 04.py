# Fazer um ciclo entre 1000 e 0 e mostrar apenas os números divisíveis por 7
cont = 1
num = 1000
while cont < num+1:
    if cont % 7 == 0:
        print(cont)