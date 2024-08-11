# ------------------------------------------ ERROS COM EXCEÇÃO -----------------------------------------------------------------

#           EXCEÇÃO	            |              CAUSA
#                               |
# AssertionError	            | Surge quando o comando assert falha
# AttributeError	            | Surge quando uma atribuição ou referência falha
# EOFError	                    | Surge quando a função input() chega na condição de fim de arquivo
# FloatingPointError	        | Surge quando uma operação de ponto flutuante falha
# GeneratorExit	                | Surge quando o método close() do gerador é chamado
# ImportError	                | Surge quando o módulo importado não é encontrado
# IndexError	                | Surge quando o índice de uma sequência está fora de alcance
# KeyError	                    | Surge quando uma chave não é encontrada no dicionário
# KeyboardInterrupt	            | Surge quando um usuário aperta o botão de interrupção (CTRL + C ou delete)
# MemoryError	                | Surge quando acaba a memória de uma operação
# NameError	                    | Surge quando uma variável não é encontrada no escopo local ou global
# NotImplementedError	        | Surge por métodos abstratos
# OSError	                    | Surge quando alguma operação de sistema causa algum erro de sistema
# OverflowError	                | Surge quando uma operação aritmética é muito grande para ser representada
# ReferenceError	            | Surge quando um proxy de referência fraco é usado para acessar um garbage collected referente
# RuntimeError	                | Surge quando um erro não se encaixa em nenhuma outra categoria
# StopIteration	                | Surge pela função next() para indicar que não há mais itens para o iterador retornar
# SyntaxError	                | Surge pelo parser quando um erro de síntaxe ocorre
# IndentationError	            | Surge quando não indentamos nosso código
# TabError	                    | Surge quando a indentação consiste em espaços e tabs impróprios
# SystemError	                | Surge quando o interpretador detecta um erro interno
# SystemExit	                | Surge pela função sys.exit()
# TypeError	                    | Surge quando uma função ou operação é aplicada a um objeto de tipo incorreto
# UnboundLocalError	            | Surge quando uma referência é feita para uma variável local em uma função ou método, porém nenhum valor está preso à variável
# UnicodeError	                | Surge quando existe um erro relacionado a Unicode codificação ou decodificação
# UnicodeEncodeError	        | Surge quando um erro de codificação de Unicode ocorre
# UnicodeDecodeError	        | Surge quando um erro de decodificação de Unicode ocorre
# UnicodeTranslateError	        | Surge quando um erro de tradução de Unicode ocorre
# ValueError	                | Surge quando uma função pega um argumento de tipo correto, porém de valor impróprio
# ZeroDivisionError	            | Surge quando a segunda divisão ou módulo é zero


# COMO TRATAR A EXCEÇÃO?

# try: quer dizer tenta
# operação

# axcept: quer dizer falha/exceto
# falha

# else: quer dizer se não teve tentativa ou falha, então mostre:

# finally: quer dizer finalmente
# certo/falha para fazer um fechamento independente do que for

try:  # tentar executar
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except: # Se falhar mostre a mensagem
# except Exception as erro: # Assim mostra qual o erro esta tendo
#    print(f'Infelizmente tivemos um problema. :(')
#    print(f'ERRO {erro.__class__}') # mostre qual erro

except (ValueError, TypeError):  # erro valor e tipo de funçao e operação é errado
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:  # erro de divisão zero do segundo
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:  # se o usuário interromper o programa antes de acabar
    print('O usuário preferiu não informar os dados!')
except Exception as erro:  # mostre a causa do erro
    print(f'O erro encontrado foi {erro.__cause__}')
else:  # Se tentou e não falhou, mostre o resultado: (opcional usar o else)
    print(f'O resultado ')
finally:  # (opcional usar o finally)
    print('Volte sempre! Muito obrigado.')