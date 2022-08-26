'''
Fuções - def em Python (Parte 2) - Return
'''

def funcao(var):
    print(var)

variavel = funcao('Valor que eu quero')
print(variavel)  # Nesse valor o var veio como none, ja que não foi atribuido nenhum valor

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

print()

def funcao(var):
    return var  # Retorna o valor da função "Valor que eu quero"

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

####################################
print()

def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2

divide = divisao(8,0)

if divide:
    print(divide)
else:
    print('Conta invalida.')

print()

def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8,4)

if divide:
    print(divide)
else:
    print('Conta invalida.')

print()

def dumb():
    return

var = dumb()
print(var, type(var))

def dumb():
    return True

var = dumb()
print(var, type(var))

def dumb():
    return 1

var = dumb()
print(var, type(var))

def dumb():
    return [1,2,3,4,5]

def dumb():
    return 'aa'

var = dumb()
print(var, type(var))

var = dumb()
print(var, type(var))

print()

def f(var):
    print(var)

def dumb():
    return f  # Escrever a função sem parenteses não a executa, so a retorna

var = dumb()
print(id(var), id(f))

if var == f:
    print('São iguais!')
else:
    print("Não são iguais.")

print()

def dumb():
    return ("Gabriel", "Kamui")

var = dumb()

print(var[1], type(var))  # Imprime duplas (listas que não podem ser alteradas)
print(var, type(var))
print(var[0], type(var))