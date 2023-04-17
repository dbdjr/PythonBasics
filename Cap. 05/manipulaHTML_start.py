# 
# Exemplo de processamento e parse de HTML
#
from html.parser import HTMLParser

class parse(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Tag de abertura encontrada.")
        if attrs.__len__() > 0 :
            for a in attrs:
                print(" Value: ", a[0], " = ", a[1])

    def handle_endtag(self, tag):
        print("Tag de fechamento encontrada.")

    def handle_comment(self, data):
        print("Tag de comentario encontrada.")

    def handle_data(self, data):
        print("Valor encontrado: ")
        if data.isspace():
            print("É um espaço")
        else:
            print("Valor encontrado é:", data)
            #for d in data:


def myOBJ():
    meuParse1 = parse()
    arq = open("D:\\git\\arquivos_de_exercicios_descubra_o_python\\Cap. 05\\exemplohtml.html","r" )
    dados = arq.read()
    meuParse1.feed(dados)

myOBJ()
