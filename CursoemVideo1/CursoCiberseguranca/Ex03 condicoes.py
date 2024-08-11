# Um script que compare 2 números e veja qual o maior ou se são iguais OK
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 == num2:
    print('Os dois valores digitados são iguais')
elif num1 >= num2:
    print('O primeiro valor é maior')
else:
    print('Segundo valor é maior')
# Um script que veja se um número é positivo, é 0, ou negativo
num = int(input("digite um numero: "))
if num >= 0:
    print("Positivo")
else:
    print("Negativo")
# Um script que veja se um aluno está aprovado ou reprovado, através da nota OK
nota = float(input('Nota do aluno: '))
if nota < 5:
    print('O aluno foi REPROVADO')
else:
    print('O aluno foi APROVADO')
# Um script que veja qual a nota que o aluno tem (Negativa, Suficiente, Bom ou Muito Bom)
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('O aluno foi REPROVADO')
elif media <= 5:
    print('O aluno está em RECUPERAÇÃO')
elif media <= 7:
    print('O aluno foi APROVADO')
elif media >= 10:
    print('O aluno obteve uma nota muita boa, APROVADO!')
