#
# Arquivo com exemplos de funções
#

# definindo uma função básica
def func1():
    print("I'm function")

func1()


# função que recebe argumentos
def func2(var1, var2):
    print(var1+ " " + var2)

func2("Felipe","Mendonça")


# função que retorna um valor
def cubo(x):
    return x**3

cub = cubo(3)
print("Essa é a raiz cubica de 3: "+ str(cub))
print("Essa é a raiz cubica de 2: "+ str(cubo(2)))
