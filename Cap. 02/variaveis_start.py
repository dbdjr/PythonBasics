
# Declarando e inicializando uma variável
f = 0 
print(f)

# declarando a mesma variável novamente
f = "abc"
print(f)#var global


print("Isto é uma string: "+ str(123))

# Variável Global X Variável local 
def funct():
    global f#declara a variavel local como global
    f = "def"
    print(f)#var local

funct()
print(f)
