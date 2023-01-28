import calendar


def calendarioHtml():

    calendarioHtml = calendar.HTMLCalendar(calendar.SUNDAY)
    r = calendarioHtml.formatmonth(2023 , 1)

    print(r)

calendarioHtml()
    

   

