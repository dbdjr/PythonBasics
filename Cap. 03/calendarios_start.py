#
# Arquivo com exemplos de uso de calendários
#

import calendar

# criando um calendário no formato texto
def CalendarioTexto():
    calendarioTexto = calendar.TextCalendar(calendar.SUNDAY)
    txtCalendario = calendarioTexto.formatmonth(2019, 6)
    print (txtCalendario)

#CalendarioTexto()
# Criando um calendário no formato HTML
i=1
def CalendarioHTML(mes):
    calendarioHTML = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlCalendario = calendarioHTML.formatmonth(2019, mes)
    print (htmlCalendario)
# loop ao longo dos dias de um mês
while(i<=12):
    CalendarioHTML(i)
    i+=1




