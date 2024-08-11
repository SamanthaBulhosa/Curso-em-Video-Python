# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os
# parênteses abertos e fechados na ordem correta.

lista = []
expr = input('Digite a expressão: ')
lista.append('(')
quan = expr.count('(')
if quan % 2:
    print('Expressão valida!')
else:
    print('Expressao invalida')

# Nao Conseguir

# COMO O PROFESSOR FEZ:

exp = str(input('Digite a expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

