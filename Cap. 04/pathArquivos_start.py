#
# Arquivo com exemplos de como trabalhar com paths
#

from os  import path
import time

def dados():
    existe = path.exists("NewArq.txt")
    diret= path.isdir("NewArq.txt")
    pathArq = path.realpath("NewArq.txt")
    pathRel= path.relpath("NewArq.txt")
    datac= time.ctime(path.getatime("NewArq.txt"))
    datamod = time.ctime(path.getmtime("NewArq.txt"))

    print(existe)
    print(diret)
    print(pathArq)
    print(pathRel)
    print(datac)
    print(datamod)

dados()