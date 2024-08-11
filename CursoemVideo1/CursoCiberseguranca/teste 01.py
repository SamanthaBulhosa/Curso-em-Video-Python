print('----- UFCD 9190 ------')
# 1 - Criar 2 variáveis do tipo string (nome e apelido) OK
nome = 'Samantha '
apelido = 'Bulhosa'
# 2 - Criar uma terceira variável que una as 2 variáveis de string e tenha um espaço entre elas (nome_completo)
nome_completo = nome + apelido
print(nome_completo)
# 3 - Criar 2 variáveis do inteiro (x e y) OK
x = int(4)
y = int(5)
# 4 - Criar uma terceira variável que seja o resultado subtração de uma variável inteira pela outra (z) OK
z = x - y
# 5 - Mostrar a divisão do x pelo z OK
print(x / y)
# 6 - Mostrar o resultado de uma comparação do x pelo y OK
print(x == y)
# 7 - Fazer 2 comparações diferentes e 1 operação lógica entre elas e mostrar o resultado OK
c1 = x <= y
c2 = x >= y
operador = c1 != c2 or c2 == c1
print(c1, c2, operador)
# 8 - Fazer o resto da divisão um pelo outro e uma operação de comparação se o valor é
# diferente de 0 e mostrar o resultado

# 9 - Mostrar a segunda letra da variável nome
print(nome[1])
# 10 - Alterar a primeira letra do apelido para um Y
altere = apelido.replace('B', 'Y')
# 11 - Criar uma variável que seja a separação da variável nome_completo pelo espaço e mostrar (nome_separado)
nome_separado = nome_completo
print(nome_separado)
# 12 - Mostrar o tamanho da variável nome_completo
print(len(nome_completo))
# 13 - Deverão mostrar o tipo da variável nome_separado
print(type(nome_separado))
# 14 - Deverão fazer comentários sobre cada um dos exercícios que estão a fazer OK
'''
1 - fiz 2 variavel e coloquei o tipo str e digitei meu nome e o apelido
2 - fiz uma variavel nome_completo, e fiz a concatenação do nome + apelido e exibir no print o resultado
3 - Criei 2 variaveis do tipo inteira e armazenei 2 valores 4 e 5 
4 - criei uma variavel z e atribuir as 2 variaveis anterior x e y e fiz a subtração como mostra no codigo acima
5 - usei a expresao / e dividir a variavel x por y
6 - usei o operador de igualdade == para comparar se x é igual a y.
7 - criei 3 variaveis e atribui operadores maior ou igual >=, menor ou igual <=, != diferente, igualdade ==
 e usei o operador logico or, exibir o resultado usando o print e colocando as variaveis.
8 - 
9 - exibir o resultado com print e fiz o fatiamente da segunda letra.
10 - alterei a letra usando a transformação replace onde substitui a letra ou palavra.
11 - criei uma variavel e coloquei .split que faz as separacoes 
12 - usei o len para conta os caracteres
13 - usei o type para ver o tipo
14 - Comentario feito! posso fazer usando '' ' ou #
15 - usei o .upper para colocar as letras em maiuscula
16 - .lower deixa as letras em menuscula
17 - 
18 - print, chamei a variavel nome_completo, e fiz o fatiamento da 2 letra ate a 6
19 - print, a variavel nome e fiz o fatiamento, 3 ate o final (vai contar 4 ate o final)
20 - coloquei o print na primeira linha
'''
# 15 - Deverão mostrar a string nome em letras grandes - OK
print(nome.upper())
# 16 - Deverão mostrar a string apelido em letras pequenas OK
print(apelido.lower())
# 17 - Deverão mostrar o x elevado a y
print(x ** y)
# 18 - Deverão mostrar na variável nome_completo, todas os caracteres entre o 2º e o 6º caracter da string OK
print(nome_completo[1:7])
# 19 - Deverão mostrar todos os caracteres do 4º caracter até ao fim, da variável nome OK
print(nome[3:])
# 20 - Deverão mostrar a frase “UFCD 9190”, no topo do programa OK
