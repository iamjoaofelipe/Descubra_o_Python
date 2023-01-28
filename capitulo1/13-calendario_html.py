import calendar


def calendarioHtml():

    calendarioHtml = calendar.HTMLCalendar(calendar.SUNDAY)
    r = calendarioHtml.formatmonth(2023 , 2)

    print(r)

calendarioHtml()
    

   

