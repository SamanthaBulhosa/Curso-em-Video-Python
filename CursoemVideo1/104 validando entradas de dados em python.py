# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor
# numérico. Ex: n = leiaInt(‘Digite um n: ‘)

# COMO O PROFESSOR FEZ:

def leiaInt(msg):
    ok = False
    valor = 0
    print('--' * 15)
    while True:
        n = str(input(msg))
        if n.isnumeric():  # isnumeric retorna um valor booliano que indica se a expressão pode ser avaliado como um número.
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

# achei difícil de entender como fazer, não entendi muito bem a explicação e a logíca no def.