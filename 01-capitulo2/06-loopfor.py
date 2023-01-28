#
# Arquivo com exemplos de Loops
#

# Definindo um LOOP FOR
def loopfor():
 for x in range(5,10):
  print(x)

loopfor()

# Usando um LOOP FOR em uma coleção

def loopArray():
    dias = ["Seg" , "Ter" , "Qua" , "Qui" , "Sex" , "Sab" , "Dom"]
    for d in dias:
        print(d)
loopArray()

# Usando a função enumerate, paara buscar valores e seus índices

def loopEnum():
    dias = ["Seg" , "Ter" , "Qua" , "Qui" , "Sex" , "Sab" , "Dom"]
    for c , d in enumerate(dias):
     print(c , d)
loopEnum()

