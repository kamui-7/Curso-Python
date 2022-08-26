"""
for/while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""

# COM WHILE

contador = 0

while contador <= 9:
    print(contador)
    contador += 1
else:
    print('Cheguei no final.')

print()

contador = 10

while contador >= 2:
    print(contador)
    contador -= 1
else:
    print('Cheguei no final.')

print()

# Com FOR

for numero in range(0, 9):
    print(numero)

print()

for numero in range(10, 1, -1):
    print(numero)

print()

# Enumerate --> Fica mais simples ainda

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)