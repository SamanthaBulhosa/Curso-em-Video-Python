def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()  # replace: substitui todas as ,virgulas por .ponto
        if entrada.isalpha() or entrada == '':
            # if entrada.isalpha() or entrada.strip() == '':
            # Se a entrada for isalpha que é (alfanumérico / letra e número).
            # OU entrada for strip que é (vazio '' ou cheia de espaço)
            print(f'\033[031mERRO: \"{entrada}\" é um preço invalido!\033[m')
        else:
            valido = True
            return float(entrada)