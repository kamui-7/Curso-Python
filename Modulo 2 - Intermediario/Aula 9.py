"""
Conjutos
# add (adciona), update(atualiza), clear, discard
# union (une)
# intersection & (todos os elementos presentes nos dois sets)
# diference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não ambos)

Sets são diferentes de dicionarios, são pares so de valores
"""

s1 = {1,2,3,4,5}

print(s1)

s1 = set()  # Para criar um set em branco
s1.add(1)
s1.add(2)
s1.add((1,2,3,'Luiz'))

print(s1)

s1.discard((1,2,3,'Luiz'))  # Retira um valor
s1.update('Python')  # Adciona, mas adciona interando todos os valores da str sem ordem

print(s1)

#  Não aceitam valores duplicados

s1 = set()
s1.update([1,2,3,4,5], {5,6,7,8})  # Une os dois sets e elimina o elemento duplicado

print(s1)

l1 = [1,2,1,1,3,4,5,6,6,6,6,6,7,8,9,'Luiz', 'Luiz']
l1 = set(l1)
l1 = list(l1)

print(l1)

print()

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2  #  Pode ser usado o union ou o |

print(s3)

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 & s2  #  Pode ser usado o intersection ou o & (pega todos em comum)

print(s3)

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 - s2  #  elementos apenas do lado esquerdo e que não estiverem no da esquerda

print(s3)

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 ^ s2  # imprime os elementos que são diferentes em ambos

print(s3)

print()

l1 = ['Gabriel', 'Marins', 'Kamui']
l2 = ['Gabriel','Kamui', 'Marins', 'Kamui', 'Marins','Gabriel','Gabriel']

# vamos fazer o casting e então ver se eles são iguais com o set que diferencia os iguais

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')