'''
Split, Join, Enumerate em Python
* Split - Divide uma String # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # int
'''

string = "O Brasil é o pais do futebol, o Brasil é penta."
lista1 = string.split(" ")
lista2 = string.split(',')

for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase.')
    
print()

string = "O Brasil é o o o o pais do futebol, o Brasil é penta."
lista1 = string.split(" ")
lista2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

# Conta a palavra o que é repetida 5x

string = "O Brasil é o pais do futebol, o Brasil é penta."
lista1 = string.split(" ")
lista2 = string.split(',')

for valor in lista2:
    print(valor.strip().capitalize()) # Remove o espaço e deixa primeira letra maiuscula.

print()

# Join

string = 'O,Brasil,é,penta.'
lista = string.split(',')
string2 = ' '.join(lista)

print(string)
print(lista)
print(string2)

print()

# Enumerate

string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

#################

lista = [
    [1, 2],
    [3, 4],
    [5, 6],
]

for v in lista:
    print(v[0], v[1]) # Ele le uma coluna da lista, por isso o v[0] e o v[1]

lista = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria'],
]

for indice, nome in lista:
    print(indice,nome)

# a função enumerate faz igual ao exemplo acima so que sem criar listas dentro de listas

lista = ['Luiz', 'João', 'Maria']

for indice, nome in enumerate(lista):
    print(indice, nome)

