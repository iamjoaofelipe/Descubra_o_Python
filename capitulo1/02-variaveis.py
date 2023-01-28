
# Declarando e inicializando uma variável
f = 0
print(f)

# declarando a mesma variável novamente
f = "abc"
print(f)

# Gerando um erro, tentando unir variáveis de tipos diferentes
print("Isto é uma string " + str(123))

# Variável Global X Variável local

def AlgumaFuncao():
    global f
    f = "def"
    print(f)

AlgumaFuncao()
print(f)

# Função que retorna um valor

def cubo(x):
    return x * x* x

f = cubo(3)
print(f)


