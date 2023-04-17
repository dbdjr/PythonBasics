# 
# Arquivo com exemplos para manipulação de dados na Internet
#

import urllib.request

def conecta():
    objurl = urllib.request.urlopen("https://www.google.com")

    if objurl.getcode()== 200:
        dados = objurl.read()
        print(dados)

conecta()
