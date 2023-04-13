#
# Exemplo de como criar classes
#

class minhaClasse():
    def __init__(self):
        self.meuAtributo = "Passou!"

    def meuMetodo(self):
        print("Passou pelo meuMetodo")

    def meuMetodo2(self, valor):
        self.outroAtributo = valor
        print(self.outroAtributo)

def criaOBJ():
    meuObj = minhaClasse()
    var1 = meuObj.meuAtributo
    print(var1)

    meuObj.meuMetodo()
    meuObj.meuMetodo2("Execut")
    
criaOBJ()