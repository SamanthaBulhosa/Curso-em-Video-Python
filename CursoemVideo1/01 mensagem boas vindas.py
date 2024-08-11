# Crie um scrip python que leia o nome de um usuário e mostre
# uma mensagem de boas-vindas de acordo com o valor digitado.

nome = input('Qual é o seu nome? ')
print('Olá,', nome, 'prazer em te conhecer!')  # aqui eu coloquei a minha variável 'nome' para mostrar na tela
print('É um prazer em te conhecer, {}!'.format(nome))  # aqui eu usei o format no final para exibir o nome
print('Olá, {}'.format(nome), 'prazer em te conhecer!')  # já aqui usei no meio da frase para mostrar como seria feito.

# acima temos 3 formas de fazer uma apresentação inserindo o nome que o usuário digitar no input
