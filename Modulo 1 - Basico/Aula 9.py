'''
For in em Python
Interando strings com for
Função range(start=0, stop, step=1)
'''

texto = 'Python'

c = 0
while c < len(texto):
    print(texto[c])
    c += 1

print()

# podemos simplificar para a função for i

for letra in texto:
    print(letra)

print()

# função range

for numero in range(10):  # (start)
    print(numero)

for numero in range(5, 10):  # (start, stop)
    print(numero)

for numero in range(5, 10, 2):  # (start, stop, step)
    print(numero)

for numero in range(20, 10, -1):
    print(numero)

print()

for numero in range(81):  # tabuada de 8
    if numero % 8 == 0:
        print(numero)

print()

texto = "Python"
nova_string = ""

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

# tambem posso usar a palavra continue e break,
# que pula para o prox. laço e a outra termina o laço.

print()

texto = "Python"
nova_string = ""

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

print()

texto = "Python"
nova_string = ""

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)