#
# Escrevendo arquivos com funções do Python
#
def escreve():
    arquivo = open("NewArq.txt","w+")

    for x in range (1,10):
        if x%2 ==0:#imprime numeros pares
            arquivo.write(str(x)+"\r\n")
            continue
    arquivo.close()
    
escreve()

def Altera():
    arquivo = open("NewArq.txt","a+")#a Append

    for x in range (1,10):
        if x%2 !=0:#imprime numeros pares
            arquivo.write(str(x)+"\r\n")
            continue
    arquivo.close()
    
Altera()

