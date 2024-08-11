# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# nao conseguir fazer! ACHEI MUITO DIFÍCIL... :(
def maior(* num):  # colocando o '* asterisco' eu sei que vou receber vários parâmetros/números e que vou desempacotar utilizando o for.
    print('=-=' * 20)
    cont = maior = soma = 0
    print(f'Analisando os valores passados...\n')  # \n é para pular a linha, sendo que se eu colocar para a esquerda pula uma linha acima
    for valor in num:  # para cada valor em número, eu vou escrever o valor.
        print(f'{valor}', end=' ')
        if cont == 0:  # Se o contador(cont) for igual a 0, ele é o maior, então faça:
            maior = valor  # minha variável maior recebe o valor que é o número
        else:
            if valor > maior:  # Verifico se o valor é maior que o maior valor
                maior = valor
            cont += 1
    print(f'Foram informados valores {cont} ao todo.')
    print(f'O maior valor informado foi {maior}')


# programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()  #
