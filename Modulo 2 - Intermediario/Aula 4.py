'''
Aula 4 - Funções (Escopo Global)
'''

variavel = 'valor'  # Escopo Global

def func():
    print(variavel)  # Escopo local

def func2():
    variavel = 'outro valor'
    print(variavel)  #Escopo local

func()
func2()

print(variavel)

print()

variavel = 'valor'  # Escopo Global

def func():
    print(variavel)  # Escopo local

def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg

func()
outra_variavel = func2(arg=variavel)

print(outra_variavel)

print()

variavel = 'valor'

def func():
    outra_variavel = 1234
    return(outra_variavel)

def func2(arg):
    print(arg)

var = func()
func2(var)