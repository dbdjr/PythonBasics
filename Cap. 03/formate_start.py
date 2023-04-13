
#
#  Arquivo com exemplos de como formatar uma data
#

from datetime import datetime

# Datas e horas podem ser formatados usando um conjunto de strings predefinidas
  
def formatHoje():
# #### Date Formatting ####
  
# # %y/%Y - Ano, %a/%A - Dia da semana, %b/%B - Mês, %d - dia do mÊs
    hoje = datetime.now()
    print("Data e hora",hoje)

    print(hoje.strftime("O Ano de hoje é: %Y"))
    print(hoje.strftime("O Dia da semana de hoje é: %A"))
    print(hoje.strftime("O Mês de hoje é: %B"))
    print(hoje.strftime("O dia de hoje é: %d"))

# formatHoje()
    

#% c - data e hora da localidade,% x - data da localidade,% X - hora da localidade
def dataLocal():
    hoje = datetime.now()
    print(hoje.strftime("O dia, data e hora local é: %c"))
    print(hoje.strftime("O data local é: %x"))
    print(hoje.strftime("A hora local é: %X"))

dataLocal()
#### Time Formatting ####
# %I/%H - 12/24 hpras, %M - minuto, %S - segundo, %p -  AM/PM

def localTime():
    hoje = datetime.now()
    print(hoje.strftime("A hora é: %I"))#12
    print(hoje.strftime("A hora é: %H"))#24

    print(hoje.strftime("Os minutos são: %M"))
    print(hoje.strftime("Os Segundos são: %S"))

    if hoje.strftime("%p") == "AM":
        print("É manhã")
    else:
        print("É tarde")

localTime()

def dataFormatada():
    hoje = datetime.now()
    print(hoje.strftime("Agora são %H:%M:%S %p"))
dataFormatada()