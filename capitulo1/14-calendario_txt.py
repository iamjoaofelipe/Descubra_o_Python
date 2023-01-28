import calendar

def calendarTexto():

    calendarTexto = calendar.TextCalendar(calendar.SUNDAY)
    r = calendarTexto.formatmonth(2023 , 1)
    
    print(r)

calendarTexto()

