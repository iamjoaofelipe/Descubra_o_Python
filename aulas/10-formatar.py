from datetime import datetime
#
#  Arquivo com exemplos de como formatar uma data
#


# Datas e horas podem ser formatados usando um conjunto de strings predefinidas

def FormatarDataHora():

    #### Date Formatting ####


    # %y/%Y - Ano, %a/%A - Dia da semana, %b/%B - Mês, %d - dia do mÊs
 hoje = datetime.now()
 print(hoje.strftime("O ano é: %y"))
 

# % c - data e hora da localidade,% x - data da localidade,% X - hora da localidade

 print(hoje.strftime("Data e hora da localidade: %c"))
#### Time Formatting ####
# %I/%H - 12/24 horas, %M - minuto, %S - segundo, %p -  AM/PM

 print(hoje.strftime("A hora atual é: %H:%M:%S %p"))
FormatarDataHora()
