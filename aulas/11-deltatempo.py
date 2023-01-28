from datetime import date
from datetime import time
from datetime import datetime
from datetime import  timedelta

def deltaTempo():
    delta = timedelta(days=10 , seconds=10 , hours=10)
    print(delta)

    hoje = datetime.now()
    print("Data do futuro:", hoje + delta)

    hoje = datetime.now()
    print("Data do passado:", hoje - delta)



deltaTempo()

    