'''
Aula 3 - Modulo 2
Funções (def) em Python - *args **kwargs
'''

def func(a1, a2, a3, a4, a5):
    print(a1, a2, a3, a4, a5)

func(1,2,3,4,5)

print()

def func(*args):
    print(args)
    print(args[0])
    print((args[-1]))

func(1,2,3,4,5)

print()

# Tuplas não podem ser alteradas então tmos que fazer um casting

def func(*args):
    for v in args:
        print(v)

func(1,2,3,4,5)

print()

def func(*args):
    print(args)

lista = [1,2,3,4,5]
lista2 = [7,8,9,10]
func(lista, 6)
func(*lista, 6)  # Desempacotei e adcionei o 6
func(lista,6,lista2)
func(*lista,6,*lista2)  # Desempacotado

print()

def func(*args, **kwargs): # Argumentos nomeados = kwargs para acessar uma str
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

lista = [1,2,3,4,5]
lista2 = [7,8,9,10]
func(*lista,6,*lista2, nome='Gabriel', sobrenome='Kamui')


print()

def func(*args, **kwargs): # Argumentos nomeados = kwargs para acessar uma str
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe.')

lista = [1,2,3,4,5]
lista2 = [7,8,9,10]
func(*lista,6,*lista2, nome='Gabriel', sobrenome='Kamui')
