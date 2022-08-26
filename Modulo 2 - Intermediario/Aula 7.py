"""
Dicionarios
Muito similar as listas, tudo o que vier apos os colchetes
"""

d1 = {'chave1':'valor da chave'}
d1['nova chave'] = 'Valor da nova chave'

print(d1)
print(d1['chave1'])

# Outro jeito de criar dicionairos mais usado

d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
d1['nova chave'] = 'Valor da nova chave'

print(d1)
print(d1['chave1'])

print()

d1 = {'chave' : 'valor', 'chave' : 'valro', 'chave' : 'Valor Real da Chave'}
print(d1)
# Note que so imprimiu um valor, o valor real pois a chave so pode ter um valor e conta o ultimo

d1 = {1 : 'valor', 2 : 'valro', 3 : 'Valor Real da Chave'}
print(d1)

print()

d1 = {
    'str' : 'valor',
    123 : 'outro valor',
    (1,2,3,4) : 'Tuplas podem ser tbm',
}

if d1.get('novo valor') is not None:
    print(d1.get('novo valor'))

print(123)

# Para adcionar um valor

d1 = {
    'str' : 'valor',
    123 : 'outro valor',
    (1,2,3,4) : 'Tuplas podem ser tbm',
}

d1['novo valor'] = 'agora ele existe'

if d1.get('novo valor') is not None:
    print(d1.get('novo valor'))

print(123)

# Para atualizar um valor no dicionario

d1 = {
    'str' : 'valor',
    123 : 'outro valor',
    (1,2,3,4) : 'Tuplas podem ser tbm',
}

d1['str'] = 'novo valor'
# d1.update( {'nova_chave':'novo_valor'})

if d1.get('str') is not None:
    print(d1.get('str'))

print(123)

# Para apagar

d1 = {
    'str' : 'valor',
    123 : 'outro valor',
    (1,2,3,4) : 'Tuplas podem ser tbm',
}

del d1['str']

print(d1)
# Para checar os valores e se eles existem
print('str' in d1)
print(123 in d1.keys())
print('outro valor' in d1.values())
print(len(d1))  # Pra saber a qauntidade

print()

d1 = {
    'chave1' : 'valor',
    'chave2' : 'outro valor',
    'chave3' : 'Tupla',
}

for k in d1:
    print(k)

for v in d1.values():
    print(v)

for k in d1.items():
    print(k)

for k in d1.items():
    print(k[0], k[1])

for k, v in d1.items():
    print(k, v)

print()

#  Criando dicionairios dentro de dicionarios

clientes = {
    'cliente1' :{
        'nome' : 'Luiz',
        'sobrenome' : 'Otavio',
    },
    'cliente2' :{
        'nome' : 'Gabriel',
        'sobrenome' : 'Marins',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

print()

d1 = { 1: 'a', 2: 'b', 3: 'c' }
v = d1

v[1] = 'Luiz'

print(d1)
print(v)

print()

#No exemplo acima o v e o d1 são iguais e no ex abaixo foi feito uma copia para serem diferentes

d1 = { 1: 'a', 2: 'b', 3: 'c' }
v = d1.copy()
v[1] = 'Luiz'

print(d1)
print(v)

print()

d1 = { 1: 'a', 2: 'b', 3: 'c', 'd' : ['Luiz', 'Otavio']}
v = d1.copy()

v[1] = 'Luiz'
v['d'][0] = 'Joãozinho'

print(d1)
print(v)

print()
# para fazer uma copia real do dicionario e necessario seguir o exemplo abaixo:

import copy

d1 = { 1: 'a', 2: 'b', 3: 'c', 'd' : ['Luiz', 'Otavio']}
v = copy.deepcopy(d1)

v[1] = 'Luiz'
v['d'][0] = 'Joãozinho'

print(d1)
print(v)

print()

# obs: tuplas são imutaveis

lista =  [
    ['c1', 1]
]

    # d1.pop(a posição do item ex:4) ---> retira um item do dicionario
    # d1.popitem()  --> elimina o ultimo elemento
    # d1.update(d2) --> concatena d1 e d2