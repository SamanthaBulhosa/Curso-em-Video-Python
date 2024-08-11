# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:  # teste
    site = urllib.request.urlopen('https://www.youtube.com/')
    # ('http://www.pudim.com.br') > acredito que por eu estar em outro país entra no except.
    # Ja com o YouTube consigo acesso ao site OK
except urllib.error.URLError:  # Se falhar / urllib.error.URLError não entendi para que serve.
    print('Não foi possível acessar ao site, verifique sua conexão com a internet.')
else:  # Se deu certo
    print(f'Acesso ao site {site.url} OK')
#    print(site.read())  # consigo ver o código inteiro do site.

# quando eu clico em RUN, demora alguns segundo para exibir o resultado, porque essa biblioteca
# urllib vai verificar se essa conexão entre o site e a internet está feita.