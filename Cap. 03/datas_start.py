#
# Arquivo com exemplos de manipulação de  data

from datetime import date
from datetime import time
from datetime import datetime

def dataHora():
    hoje = date.today()
    print("Hoje é: ", hoje)
    print("Hoje é: ", hoje.day, hoje.month, hoje.year)
    print("Hoje é: ", hoje.weekday())
    dias = ["seg","ter","qua","qui","sex","sab","dom"]
    print("Hoje é: ", dias[hoje.weekday()])

    data= datetime.now()
    print("Data e hora", data)
    tempo = datetime.time(data)
    print("Hora atual: ", tempo)
dataHora()