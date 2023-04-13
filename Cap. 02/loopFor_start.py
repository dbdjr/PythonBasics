#
# Arquivo com exemplos de Loops
#

# Definindo um LOOP FOR
def loopFor():
    for x in range(5,10):#range serve para limitar um intervalo                 
        print(x)   

loopFor()

# Usando um LOOP FOR em uma coleção
def loopArray ():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    for d in dias:#dias usado com range
        print (d)

loopArray()


# Usando BREAK e CONTINUE


# Usando a função enumerate, paara buscar valoeres e seus índices
def loopEnum ():
    dias = ["dom","seg", "ter", "qua", "qui", "sex", "sab"]
    for i, d in enumerate(dias):#enumarate cria um indice para cada elemento do array
        print (i, d)

loopEnum()