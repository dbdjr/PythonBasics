#
# Exemplo de como usar os comando Break e Continue
#
def loopb():
    for x in range (5,10):
        if x==7:
            break
        print("valor de x é:", x )
loopb()

def loopImp():
    for x in range (1,10):
        if x%2 ==0:#imprime numeros par
            continue #interrompe apenas quando o if é verdadeiro mas continua o loop
        print("valor de x é:", x )
    
loopImp()