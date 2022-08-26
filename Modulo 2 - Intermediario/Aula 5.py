'''
Aula 5
'''

def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)

# Com a função lambda o valor retornado é o msmo.

a = lambda x, y: x * y
print(a(2,2))

print()

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

def func(item):
    return item[1]

lista.sort(key=func, reverse=True)   # Ordenar do maior pro menor
print(lista)

print()

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

lista.sort(key=lambda item: item[1],)  # Ordenar do menor por maior
print(lista)

print()

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista, key=lambda i: i[0]))
print(sorted(lista, key=lambda i: i[1]))
print(lista)