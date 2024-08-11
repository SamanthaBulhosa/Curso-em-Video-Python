# DICIONÁRIOS

"pessoas = ()  # tuplas"""
"pessoas = []  # listas"

pessoas = {'nome': 'Samantha', 'sexo': 'F', 'idade': 25}  # dicionários
print(pessoas)  # exibe tudo do dicionario: {'nome': 'Samantha', 'sexo': 'F', 'idade': 25}
# print(pessoas[0])  # se eu colocar elemento [0], vai dar erro por conta de se um nome
print(pessoas['idade'])  # o corretor é colocar [idade] para exibir ao invés do número
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')  # utilizando um print formatado para exibir nome e idade
# OBS: PRECISO COLOCAR ASPA "DUPLA", SENÃO DAR ERRO!

# ---------CHAMANDO OS ELEMENTOS DENTRO DO DICIONÁRIO -----------

print(pessoas.values())  # valores --> dict_values(['Samantha', 'F', 25])
print(pessoas.keys())    # chaves  --> dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.items())   # itens ---> dict_items([('nome', 'Samantha'), ('sexo', 'F'), ('idade', 25)])

# ----- LAÇO ----------

for k in pessoas.keys():  # criei a variável 'k' para representar o keys e vai ser exibido 'nome,sexo,idade'.
    print(k)
for k, v in pessoas.items():  # faço a junção dos 2, conseguindo formatar o print para exibir o dado conforme a msg
    print(f'{k} = {v}')

# ------ DELETANDO UM ITEM DO DICIONARIO -------

pessoas = {'nome': 'Samantha', 'sexo': 'F', 'idade': 25}
del pessoas['sexo']  # o 'sexo F' foi deletado, sendo exibido somente nome: Samantha e idade: 25
pessoas['nome'] = 'Raiana'  # posso modificar o nome
pessoas['peso'] = 42.08  # posso adicionar um elemento sem precisar utilizar o append
for k, v in pessoas.items():
    print(f'{k}: {v}')

# ------------------------------------------------
estado = dict()
brasil = list()
for conte in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # nao posso fazer [:] uma copía do fatiamento, preciso usar o método 'copy'
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
        # vai ser exibido assim ao executar essa linha de código.
        """ O campo UF tem valor Bahia.
            O campo Sigla tem valor BA.
            O campo UF tem valor Sao paulo.
            O campo Sigla tem valor SP.
            O campo UF tem valor Rio de janeiro .
            O campo Sigla tem valor RJ."""
for e in brasil:
    for v in e.values():
        print(f'{v}.', end='')
    print()  # print vazio para pular a linha