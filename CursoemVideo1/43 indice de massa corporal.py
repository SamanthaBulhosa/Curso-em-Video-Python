# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
# e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

# Pesquisar a massa corporia como fazer calculo indice
""" Como calcular IMC Para calcular o Índice de Massa Corporal, basta seguir a fórmula seguinte:
# peso / (altura x altura). Ou seja, deve multiplicar a sua altura por ela própria e, depois,
# dividir o peso por esse resultado . """

peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
multiplicar = altura * altura
dividir = peso / multiplicar
print('O seu IMC é {:.1f}'.format(dividir))
if dividir <= 18.5:
    print('Abaixo do peso')
elif dividir <= 25:
    print('Peso ideal')
elif dividir <= 30:
    print('Sobrepeso')
elif dividir <= 40:
    print('Obesidade')
else:
    print('Obesidade morbida')

# Como o PROFESSOR FEZ:

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)  # aqui ele dividiu a altura por 2 e depois dividiu pelo peso
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do PESO normal')
# elif imc >= 18.5 and imc < 25:  Pode tmb fazer dessa forma
elif 18.5 <= imc < 25:
    print('PARABÈNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
