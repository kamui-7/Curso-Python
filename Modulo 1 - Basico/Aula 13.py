'''
Desempacotamento de Listas e Python
'''

lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista

print(n2)

# O numero de variaveis tem que ser igual ao numero de itens na lista, senão retorna em erro.
# Mas se colocar *outra_lista, criando assim outra lista, daria certo, por exemplo

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7]

n1, n2, n3, *outra_lista = lista

print(n3)
print(n2)
print(n1)
print(outra_lista)

# Para imprimir o ultimo da lista devemos colocar apos a lista criada

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7]

n1, n2, n3, *outra_lista, n_ultimo = lista

print(n_ultimo)

# *_ é usado para mostrar aos desenvolvedores que o restante da lista não sera utilizado

########################################

'''
Trocando o valor de duas variaveis em Python
'''

x = 10  # Tem que virar Luiz
y = 'Luiz'  # Tem que virar 10

# Ou seja x tem que virar y e y tem que virar x

z = x
x = y
y = z

print(x, y)

#  No python tem uma maneira mias simples de se fazer isso

x = 10
y = 'Luiz'
x, y = y, x

print(x, y)

x = 10
y = 'Luiz'
z = 77
x, y, z = z, x, y

print(x, y, z)
