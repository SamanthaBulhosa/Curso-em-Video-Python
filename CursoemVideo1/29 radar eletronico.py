# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h. mostre uma mensagem dizendo que ele foi multado.
# A multa vai custa R$7,00 por cada Km acima do limite.


vel = float(input('Qual é a velocidade atual de um carro? '))
if vel > 80:  # ultilizando somente o if é uma condiçao simples
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (vel - 80) * 7  # retirei o 80 do km e o restante que exceder vai contar
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print("Tenha um bom dia, dirija com segurança!")
