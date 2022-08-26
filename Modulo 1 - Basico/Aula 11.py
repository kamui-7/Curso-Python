'''
For/Eles em Python
'''
# no for pode ter tambem o:
# break --> muda para o proximo laço
# continue --> muda para a proxima interação do laço

variavel = ['Gabriel', 'Kamuizinho', 'Guilherme']

for valor in variavel:
    if valor.startswith('K'):
        print("Começa com K: ", valor)
    else:
        print('Não começa com K: ', valor)

print()

variavel = ['Gabriel', 'Kamuizinho', 'Guilherme']

comeca_k = False

for valor in variavel:
    if valor.startswith('K'):
        comeca_k = True

if comeca_k:
    print('Existe uma plavra que começa com K.')
else:
    print('Não existe uma pavra que começe com K.')

