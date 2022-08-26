'''
Listas em Python
fatiamento --> [Inicio:fim:step]
append, insert, pop, del, clear, extend, min, max
range
'''

#         0    1    2    3    4    5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#     -   6    5    4    3    2    1

string = 'ABCDE'

print(lista[1])  # Imprime o item de uma lista, seja ele str, int,bool ou float.
print(string[1])  # Imprime uma parte da string, no caso somente o B.

lista[5] = "Qualquer outra coisa."  # Dessa forma pode se mudar o item da lista, no caso 10.5 vira a string abaixo.
print(lista[5])
print(lista[0:3])  # O numero onde ele para não aparece, por isso o 3 não é mostrado.

print()

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2  # concatena as duas variaveis l1 e l2

print(l1)
print(l2)
print(l3)

print()

print( max(l3) )  # Retorna o maior valor da lista
print( min(l3) )  # Retorna o menor valor da lista

print()

l1.extend(l2)  # adciona a l2 na l1
print(l2)
l2.append('b')  # insere a string b na l2
print(l2)
l2.insert(0, "Zero")  # Inseriu a string Zero na posição 0 da l2
print(l2)
del(l2[3:4])  # O comando del , retira o valor de indice 4, que é o int 6
print(l2)

print()

l2 = list(range(0, 100, 8))
print(l2)

print()

l2 = [0,1,2,3,4,5,6,7,8,9,10]

for elem in l2:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}.')

print()

secreto = "termo"
digitadas = []
chance = 4

while True:
    if chance <= 0:
        print('Voce perdeu!!!!')
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Ah isso não vale, digite uma letra.")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhulll! A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFF... A letra "{letra}" não existe na palavra secreta')
        digitadas.pop()  # O pop remove o ultimo elemento adcionado na lista.

    secreta_temporaria = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreta_temporaria += letra_secreta
        else:
            secreta_temporaria += "*"

    if secreta_temporaria == secreto:
        print('Voce acertou.')
        break
    else:
        print(f'A palvra esta assim: {secreta_temporaria}')

    if letra not in secreto:
        chance -= 1

    print(f'Voce ainda tem {chance} chances.')
    print()