from datetime import date
from datetime import time
from datetime import datetime

def ManipulandoHoraData():
    hoje = date.today()
    print("Hoje é dia: " , hoje)

    print("Partes da data: " , hoje.day , hoje.month , hoje.year)
    
    print("Número do dia da semana:" , hoje.weekday())

    dias = ("Seg" , "Ter" , "Qua" , "Qui" , "Sex" , "Sáb" , "Dom")
    print("Nome do dia da semana abreviado: ", dias[hoje.weekday()])

    data = datetime.now()
    print("Data e Hora", data)
    
    tempo = datetime.time(data)
    print("Horario atual: ", tempo)
ManipulandoHoraData()
