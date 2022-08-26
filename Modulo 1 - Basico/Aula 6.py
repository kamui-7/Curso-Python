'''
Aula 6 -  Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Numeros de pontos flutuantes (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
'''

nome = "Gabriel Marins"
nome_formatado = '{:0^20}'.format(nome) # Usado o ^ para por o 0 no centro do nome
print(nome_formatado)

'''
Manipulando Strings - Aula 6

*String Indices
*Fatiamento de Strings
*Funções Built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
'''

# indices positivos  [012345678]
texto =              'Python s2'
# indices negativos -[987654321]
site = 'www.google.com.br/'

print(texto[8])  # Retorna 2 que é o 8 positivo
print(texto[-1])  # Retorna o 2 que é o 1 negativo
print(site[:-1])  # Aqui fizemos um fatiamento e escolhemos a posição -1 para ser retirada
print(site[4:10])  # O fatiamento é da seguinte forma [inicio:fim]
print(site[0::4])  # Aqui a formula é [inicio:fim:pula de x em x espaço, um passo]



