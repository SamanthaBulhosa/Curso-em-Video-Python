# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
# retornar um dicionário com as seguintes informações:

# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*n, sit=False):  # *n é para receber várias notas, sit=False por padrão para não adicionar a situação
    """
    — > Função para analisar notas e situações de vários alunos.
    :param n: Um ou mais notas dos alunos (aceita várias notas)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = dict()
    dicionario['total'] = len(n)  # len ver quantos notas foram informados.
    dicionario['maior'] = max(n)  # max ver qual o maior nota.
    dicionario['menor'] = min(n)  # min ver qual a menor nota.
    dicionario['média'] = sum(n) / len(n)  # sum faz a soma, / divide pelo len(n) que é a quantidade notas
    if sit:  # Essa situação so vai ser adicionada se for sit=True
        if dicionario['média'] >= 7:  # se a média for maior ou igual a 7, faça:
            dicionario['situação'] = 'BOA'
        elif dicionario['média'] >= 5:  # se a média for maior ou igual a 5, faça: (lembrando que vai do 5 até 6 por conta que eu tenho o if acima informando outra condição)
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'
    return dicionario  # return me dar o retorno das informações que esta no dicionário.


# Programa Principal
resp = notas(5.5, 2.5, 1.5, 8.5, sit=True)  # Resultado mostrando com sit=True abaixo:
# {'total': 4, 'maior': 8.5, 'menor': 1.5, 'média': 4.5, 'situação': 'RUIM'}
'''resp = notas(5.5, 2.5, 1.5, 8.5)'''  # Resultado mostrando sem o sit=True abaixo:
# {'total': 4, 'maior': 8.5, 'menor': 1.5, 'média': 4.5}
print(resp)
help(notas)
