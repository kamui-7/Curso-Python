'''
While/Else - Aula 8
contadores e acumuladores
'''

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no final.')

'''
Iterando strings com while em Python
Iterar é o ato de percorrer todas as letras da string
'''

#          Indices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'  # Iteravel
tamanho_frase = len(frase)
contador = 0
nova_string = ''

#  Iteração <- Iterar
while contador < tamanho_frase:
    # print(frase[contador], contador)
    nova_string += frase[contador]
    print(nova_string)
    contador += 1

print(nova_string)

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
        print(nova_string)
    contador += 1

print(nova_string)