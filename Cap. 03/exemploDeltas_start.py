#
# Arquivo de exemplo para uso da classe timedeltas
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def quantosFaltam(ano, mes, dia):
    hoje  = date.today()
    dataProcurada = date(ano,mes,dia)
    if dataProcurada > hoje:
        data = dataProcurada - hoje
        mensagem = "Faltam "+ str(data).replace("days, 0:00:00","")+"dias"
        return mensagem
    elif dataProcurada < hoje:
        d = dataProcurada - hoje
        data = str(d).replace("days, 0:00:00", "")
        mensagem = "Passaram " + data.replace("-","")+"dias"
        return mensagem
    else:
        mensagem = "A data é hoje!"
        return mensagem
    
print(quantosFaltam(2022,4,13))
