# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santos".

cid = str(input('Em qual cidade voce nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')

# Com o .strip eu removo todos os espaços
# Em cid[:5] eu nao falo onde comeca e mando ir ate o numero 5 de caracteres
# No .upper() eu consigo fazer com que o nome Santo seja verdadeiro independente de como o usuario digitar ex: SaNTo
# vai dar True
