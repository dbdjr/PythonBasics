#
# Arquivo com exemplos de uso de calendários
#
import calendar

def imprimeMes():
    for mes in calendar.month_name:
        print(mes)
    for dias in calendar.day_name:
        print(dias)

imprimeMes()