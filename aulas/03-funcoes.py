#
# Arquivo com exemplos de funções
#

# Definindo uma função básica
def funcao1():
    print("Eu sou uma função")

funcao1()

# Função que recebe argumentos
def funcaoargumento(argumento1,argumento2):
    print(argumento1+ " " + argumento2)
funcaoargumento("João" , "Felipe")

# Função que retorna um valor

def funcaovalor(x):
    return x * x * x
valor = funcaovalor(3)
print(valor)
print(funcaovalor(10))




