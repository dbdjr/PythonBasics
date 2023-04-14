#
# Lendo arquivos com funções do Python
#
def ler():
    arquivo = open("NewArq.txt","r")#r read
    if(arquivo.mode =="r"):
        conteudo=arquivo.read()
        print(conteudo)
    arquivo.close()
##ler()

def lerGrandeArq():#ler linha a linha
    arquivo = open("NewArq.txt","r")#r read
    if(arquivo.mode =="r"):
        conteudoTotal= arquivo.readlines()
        for conteudo in conteudoTotal:
            print(conteudo)
    arquivo.close()
ler()