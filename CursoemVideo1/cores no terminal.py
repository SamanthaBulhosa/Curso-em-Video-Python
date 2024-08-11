

print('\033[0:30:41m Teste')  # Nenhum estilo, texto branco e fundo vermelho
print('\033[4:33:44m Teste')  # Sublinhado, texto amarelo e fundo azul
print('\033[1:35:43m Texte')  # Negrito, texto azul, fundo amarelo
print('\033[30:42m Texto')    # Texto branco e fundo verde
print('\033[m Texto')         # Remove toda configuração
print('\033[7:40m Texto')     # Inverter o fundo vai ficar branco e o texto preto

a = 25
b = 26
print('\033[mTenho \033[1:35:40m{}\033[m e vou fazer \033[1:30:45m{}\033[m no dia 04/11/2023'.format(a, b))

nome = 'Samantha'
print('Olá! Multo prazer em te conhecer, {}{}{}!!!'.format('\033[4:34m', nome, '\033[m'))

nome = 'Samantha'
cores = {'limpa': '\033{m',
         'azul': '\033[34m]',
         'amarelo': '\033[33m',
         'roxo': '\033[7:35:40m'}

print('Olá! Multo prazer em te conhecer, {}{}{}!!!'.format(cores['roxo'], nome, cores['amarelo']))
