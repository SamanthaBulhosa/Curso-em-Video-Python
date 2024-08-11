# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilidadesexterno import moedapacote
from utilidadesexterno import dadospacote

# p = float(input('Digite o preço: R$')) Altero essa linha para a de baixo ja que estou
p = dadospacote.leia_dinheiro('Digite o preço: R$')  # vai me retornar como um input so que fazendo uma verificação
moedapacote.resumo(p, 35, 22)