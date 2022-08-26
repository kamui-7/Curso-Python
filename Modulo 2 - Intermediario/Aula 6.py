'''
Tuplas(Tuple)
'''

t1 = (1,2,3, 'a', 'Luiz Otavio')


print(t1)

t1 = 1,2,3,4,5
t2 = 6,7,8,9,0
t3 = t1 + t2

print(t3)

t1 = 1,2,3,4,5
t2 = 'Kamui',7,8,9,0
t3 = t1 + t2

n1, n2, n3, n4, n5, n6, *_ = t3

print(n6)

# Pode colocar o mulytiplicador e multiplicar as tupla para serem mostradas varias vezes.

# Converter tuplas em listas

t1 = (1,2,3,4,5)
t1 = list(t1)
t1[1] = 3000
print(t1)

t1 = tuple(t1)
print(t1)